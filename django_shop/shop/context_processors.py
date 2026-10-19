from .models import Cart


def cart_context(request):
    """Контекст-процессор для корзины"""
    session_key = request.session.session_key
    if session_key:
        try:
            cart = Cart.objects.get(session_key=session_key)
            return {
                'cart_count': cart.total_items,
                'cart_total': cart.total_price,
            }
        except Cart.DoesNotExist:
            pass
    return {'cart_count': 0, 'cart_total': 0}
