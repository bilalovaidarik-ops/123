from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.models import Q
from .models import Category, Product, Cart, CartItem, Order, OrderItem
from .forms import OrderForm
import json


def get_or_create_cart(request):
    """Получить или создать корзину"""
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


# 1. Главная страница
@ensure_csrf_cookie
def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(available=True)[:8]
    sale_products = Product.objects.filter(available=True, old_price__isnull=False)[:4]
    context = {
        'categories': categories,
        'featured_products': featured_products,
        'sale_products': sale_products,
    }
    return render(request, 'index.html', context)


# 2. Список всех товаров
@ensure_csrf_cookie
def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    # Фильтрация по цене
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    # Сортировка
    sort = request.GET.get('sort', '-created_at')
    if sort in ['price', '-price', 'name', '-name', '-created_at']:
        products = products.order_by(sort)
    context = {
        'products': products,
        'categories': categories,
        'current_sort': sort,
    }
    return render(request, 'product_list.html', context)


# 3. Детальная страница товара
@ensure_csrf_cookie
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)


# 4. Товары по категории
@ensure_csrf_cookie
def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
    }
    return render(request, 'category.html', context)


# 5. Корзина
@ensure_csrf_cookie
def view_cart(request):
    cart = get_or_create_cart(request)
    items = cart.items.select_related('product').all()
    context = {
        'cart': cart,
        'items': items,
    }
    return render(request, 'cart.html', context)


# 6. AJAX: Добавить в корзину
@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Product, id=product_id, available=True)
    cart = get_or_create_cart(request)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity
    item.save()
    return JsonResponse({
        'success': True,
        'message': f'{product.name} добавлен в корзину',
        'cart_count': cart.total_items,
        'cart_total': str(cart.total_price),
    })


# 7. AJAX: Обновить количество в корзине
@require_POST
def update_cart_item(request):
    item_id = request.POST.get('item_id')
    quantity = int(request.POST.get('quantity', 1))
    item = get_object_or_404(CartItem, id=item_id)
    if quantity > 0:
        item.quantity = quantity
        item.save()
        return JsonResponse({
            'success': True,
            'item_total': str(item.total_price),
            'cart_total': str(item.cart.total_price),
            'cart_count': item.cart.total_items,
        })
    else:
        item.delete()
        return JsonResponse({
            'success': True,
            'removed': True,
            'cart_total': '0.00',
            'cart_count': 0,
        })


# 8. AJAX: Удалить из корзины
@require_POST
def remove_from_cart(request):
    item_id = request.POST.get('item_id')
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    cart = get_or_create_cart(request)
    return JsonResponse({
        'success': True,
        'message': 'Товар удалён из корзины',
        'cart_total': str(cart.total_price),
        'cart_count': cart.total_items,
    })


# 9. Оформление заказа
def checkout(request):
    cart = get_or_create_cart(request)
    items = cart.items.select_related('product').all()
    if not items.exists():
        return redirect('shop:view_cart')
    form = OrderForm()
    context = {
        'cart': cart,
        'items': items,
        'form': form,
    }
    return render(request, 'checkout.html', context)


# 10. AJAX: Обработка заказа
@require_POST
def process_order(request):
    cart = get_or_create_cart(request)
    items = cart.items.select_related('product').all()
    if not items.exists():
        return JsonResponse({'success': False, 'message': 'Корзина пуста'}, status=400)
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save(commit=False)
        order.total_price = cart.total_price
        order.save()
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
            )
            # Уменьшаем остаток на складе
            product = item.product
            product.stock -= item.quantity
            product.save()
        # Очищаем корзину
        items.delete()
        return JsonResponse({
            'success': True,
            'message': 'Заказ оформлен!',
            'order_id': order.id,
            'redirect_url': f'/order-success/{order.id}/'
        })
    else:
        errors = form.errors.as_json()
        return JsonResponse({'success': False, 'errors': json.loads(errors)}, status=400)


# 11. Страница успешного заказа
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'order_success.html', context)


# 12. AJAX: Поиск товаров
def search_products(request):
    query = request.GET.get('q', '')
    if len(query) >= 2:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query),
            available=True
        )[:10]
        results = [{
            'id': p.id,
            'name': p.name,
            'price': str(p.price),
            'slug': p.slug,
            'image': p.image.url if p.image else '',
        } for p in products]
        return JsonResponse({'results': results, 'count': len(results)})
    return JsonResponse({'results': [], 'count': 0})


# 13. История заказов
def user_orders(request):
    email = request.GET.get('email', '')
    orders = []
    if email:
        orders = Order.objects.filter(email=email).prefetch_related('items__product')
    context = {'orders': orders, 'email': email}
    return render(request, 'user_orders.html', context)


# 14. Детали заказа
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.items.select_related('product').all()
    context = {'order': order, 'items': items}
    return render(request, 'order_detail.html', context)


# 15. AJAX: Количество товаров в корзине
def api_cart_count(request):
    cart = get_or_create_cart(request)
    return JsonResponse({
        'count': cart.total_items,
        'total': str(cart.total_price),
    })
