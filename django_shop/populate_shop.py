#!/usr/bin/env python
"""
Скрипт для заполнения базы данных тестовыми данными.
Запуск: python populate_shop.py
"""
import os
import sys
import django

# Настройка Django окружения
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from shop.models import Category, Product
from django.contrib.auth.models import User


def populate():
    print("Начинаю заполнение базы данных...")

    # Создание суперпользователя
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@shop.ru', 'admin123')
        print("✓ Создан суперпользователь: admin / admin123")
    else:
        print("→ Суперпользователь уже существует")

    # Категории
    categories_data = [
        {'name': 'Электроника', 'slug': 'electronics', 'description': 'Смартфоны, ноутбуки, планшеты и другие гаджеты'},
        {'name': 'Одежда', 'slug': 'clothing', 'description': 'Мужская и женская одежда, обувь и аксессуары'},
        {'name': 'Книги', 'slug': 'books', 'description': 'Художественная литература, учебники и бизнес-литература'},
        {'name': 'Спорт', 'slug': 'sports', 'description': 'Спортивное оборудование и инвентарь'},
        {'name': 'Дом и сад', 'slug': 'home-garden', 'description': 'Товары для дома, ремонта и сада'},
        {'name': 'Игрушки', 'slug': 'toys', 'description': 'Игрушки для детей всех возрастов'},
    ]

    categories = {}
    for cat_data in categories_data:
        cat, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name'], 'description': cat_data['description']}
        )
        categories[cat_data['slug']] = cat
        status = "✓" if created else "→"
        print(f"{status} Категория: {cat.name}")

    # Товары
    products_data = [
        # Электроника
        {'name': 'Смартфон Galaxy Pro Max', 'slug': 'galaxy-pro-max', 'category': 'electronics',
         'price': 79990, 'old_price': 89990, 'stock': 25,
         'description': 'Флагманский смартфон с AMOLED дисплеем 6.7", процессором Snapdragon 8 Gen 3, камерой 200 МП и батареей 5000 мАч.'},
        {'name': 'Ноутбук UltraBook 15', 'slug': 'ultrabook-15', 'category': 'electronics',
         'price': 129990, 'old_price': 149990, 'stock': 15,
         'description': 'Тонкий и лёгкий ноутбук с процессором Intel Core i7, 16 ГБ RAM, SSD 512 ГБ, IPS экран 15.6".'},
        {'name': 'Беспроводные наушники SoundMax', 'slug': 'soundmax-wireless', 'category': 'electronics',
         'price': 12990, 'old_price': 15990, 'stock': 50,
         'description': 'Наушники с активным шумоподавлением, время работы до 30 часов, поддержка Bluetooth 5.3.'},
        {'name': 'Планшет TabPro 11', 'slug': 'tabpro-11', 'category': 'electronics',
         'price': 54990, 'old_price': None, 'stock': 20,
         'description': 'Планшет с экраном 11" 2K, процессором M2, 128 ГБ памяти, поддержка стилуса.'},
        {'name': 'Умные часы FitWatch 5', 'slug': 'fitwatch-5', 'category': 'electronics',
         'price': 24990, 'old_price': 29990, 'stock': 35,
         'description': 'Смарт-часы с GPS, пульсометром, SpO2 датчиком. Водозащита IP68, до 14 дней работы.'},

        # Одежда
        {'name': 'Куртка зимняя Arctic', 'slug': 'arctic-jacket', 'category': 'clothing',
         'price': 15990, 'old_price': 19990, 'stock': 30,
         'description': 'Тёплая зимняя куртка с утеплителем Thinsulate, водоотталкивающая ткань, капюшон с мехом.'},
        {'name': 'Джинсы Classic Fit', 'slug': 'classic-jeans', 'category': 'clothing',
         'price': 4990, 'old_price': None, 'stock': 100,
         'description': 'Классические джинсы прямого кроя из плотного денима, 100% хлопок.'},
        {'name': 'Кроссовки RunFast Pro', 'slug': 'runfast-pro', 'category': 'clothing',
         'price': 8990, 'old_price': 11990, 'stock': 45,
         'description': 'Беговые кроссовки с амортизацией, дышащий верх, подошва из пены EVA.'},
        {'name': 'Рубашка Oxford', 'slug': 'oxford-shirt', 'category': 'clothing',
         'price': 3490, 'old_price': None, 'stock': 60,
         'description': 'Классическая рубашка из хлопка Oxford, приталенный крой, воротник на пуговицах.'},

        # Книги
        {'name': 'Мастер и Маргарита', 'slug': 'master-margarita', 'category': 'books',
         'price': 590, 'old_price': 790, 'stock': 200,
         'description': 'Роман Михаила Булгакова. Подарочное издание в твёрдом переплёте.'},
        {'name': 'Чистый код', 'slug': 'clean-code', 'category': 'books',
         'price': 1290, 'old_price': None, 'stock': 80,
         'description': 'Роберт Мартин. Руководство по созданию читаемого, понятного и поддерживаемого кода.'},
        {'name': 'Думай медленно, решай быстро', 'slug': 'think-fast-slow', 'category': 'books',
         'price': 690, 'old_price': 890, 'stock': 150,
         'description': 'Даниэль Канеман. О двух системах мышления и принятии решений.'},

        # Спорт
        {'name': 'Гантели разборные 20 кг', 'slug': 'dumbbells-20kg', 'category': 'sports',
         'price': 5990, 'old_price': 7490, 'stock': 25,
         'description': 'Набор разборных гантелей общим весом 20 кг, обрезиненные блины, хромированный гриф.'},
        {'name': 'Коврик для йоги Premium', 'slug': 'yoga-mat-premium', 'category': 'sports',
         'price': 2490, 'old_price': None, 'stock': 70,
         'description': 'Нескользящий коврик 183x61 см, толщина 6 мм, экологичный материал TPE.'},
        {'name': 'Велосипед горный Trail 29', 'slug': 'trail-29-bike', 'category': 'sports',
         'price': 45990, 'old_price': 52990, 'stock': 10,
         'description': 'Горный велосипед с алюминиевой рамой, 21 скорость, дисковые тормоза, колёса 29".'},

        # Дом и сад
        {'name': 'Робот-пылесос CleanBot X1', 'slug': 'cleanbot-x1', 'category': 'home-garden',
         'price': 29990, 'old_price': 34990, 'stock': 18,
         'description': 'Робот-пылесос с лидаром, влажная уборка, управление через приложение, время работы 180 мин.'},
        {'name': 'Набор садовых инструментов', 'slug': 'garden-tools-set', 'category': 'home-garden',
         'price': 3490, 'old_price': None, 'stock': 40,
         'description': '12 предметов: лопата, грабли, секатор, перчатки и другие инструменты в сумке.'},
        {'name': 'Светильник LED потолочный', 'slug': 'led-ceiling-light', 'category': 'home-garden',
         'price': 4990, 'old_price': 6490, 'stock': 30,
         'description': 'Потолочный LED светильник 48W, регулировка яркости и цветовой температуры, пульт ДУ.'},

        # Игрушки
        {'name': 'Конструктор МегаБлок 500', 'slug': 'megablock-500', 'category': 'toys',
         'price': 3990, 'old_price': 4990, 'stock': 55,
         'description': 'Конструктор из 500 деталей, совместим с LEGO, для детей от 6 лет.'},
        {'name': 'Радиоуправляемая машина Monster', 'slug': 'monster-rc-car', 'category': 'toys',
         'price': 6990, 'old_price': None, 'stock': 20,
         'description': 'Внедорожник на радиоуправлении, скорость до 40 км/ч, полный привод, аккумулятор в комплекте.'},
        {'name': 'Настольная игра Стратегия', 'slug': 'strategy-board-game', 'category': 'toys',
         'price': 2490, 'old_price': 2990, 'stock': 35,
         'description': 'Экономическая стратегия для 2-6 игроков, время партии 60-120 минут, возраст 10+.'},
    ]

    for prod_data in products_data:
        category = categories[prod_data['category']]
        old_price = prod_data.get('old_price')
        product, created = Product.objects.get_or_create(
            slug=prod_data['slug'],
            defaults={
                'name': prod_data['name'],
                'category': category,
                'price': prod_data['price'],
                'old_price': old_price,
                'stock': prod_data['stock'],
                'description': prod_data['description'],
                'available': True,
            }
        )
        status = "✓" if created else "→"
        print(f"{status} Товар: {product.name} - {product.price} ₽")

    print(f"\n{'='*50}")
    print(f"Заполнение завершено!")
    print(f"Категорий: {Category.objects.count()}")
    print(f"Товаров: {Product.objects.count()}")
    print(f"{'='*50}")
    print(f"\nДля запуска сервера: python manage.py runserver")
    print(f"Админ-панель: http://127.0.0.1:8000/admin/")
    print(f"Логин: admin / admin123")


if __name__ == '__main__':
    populate()
