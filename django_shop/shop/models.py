from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Категория товаров"""
    name = models.CharField('Название', max_length=200, db_index=True)
    slug = models.SlugField('Слаг', max_length=200, unique=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""
    name = models.CharField('Название', max_length=200, db_index=True)
    slug = models.SlugField('Слаг', max_length=200, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='products', verbose_name='Категория'
    )
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    old_price = models.DecimalField('Старая цена', max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField('Остаток', default=0)
    available = models.BooleanField('Доступен', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.name

    @property
    def discount_percent(self):
        if self.old_price and self.old_price > self.price:
            return int((self.old_price - self.price) / self.old_price * 100)
        return 0


class Cart(models.Model):
    """Корзина"""
    session_key = models.CharField('Ключ сессии', max_length=40, db_index=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина #{self.id}'

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())


class CartItem(models.Model):
    """Элемент корзины"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField('Количество', default=1)
    added_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

    def __str__(self):
        return f'{self.product.name} x{self.quantity}'

    @property
    def total_price(self):
        return self.product.price * self.quantity


class Order(models.Model):
    """Заказ"""
    STATUS_CHOICES = [
        ('pending', 'Ожидает обработки'),
        ('processing', 'В обработке'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    ]

    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20)
    address = models.CharField('Адрес', max_length=250)
    city = models.CharField('Город', max_length=100)
    postal_code = models.CharField('Почтовый индекс', max_length=20)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField('Итого', max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заказ #{self.id} - {self.first_name} {self.last_name}'


class OrderItem(models.Model):
    """Элемент заказа"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return f'{self.product.name} x{self.quantity}'

    @property
    def total_price(self):
        return self.price * self.quantity
