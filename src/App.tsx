import { useState } from 'react'

function App() {
  const [activeTab, setActiveTab] = useState('overview')

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Header */}
      <header className="border-b border-white/10 backdrop-blur-sm bg-black/20">
        <div className="max-w-7xl mx-auto px-6 py-6">
          <div className="flex items-center gap-4">
            <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center">
              <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 100 4 2 2 0 000-4z" />
              </svg>
            </div>
            <div>
              <h1 className="text-3xl font-bold text-white">ShopMart</h1>
              <p className="text-purple-300">Интернет-магазин на Django + Bootstrap 5 + AJAX</p>
            </div>
          </div>
        </div>
      </header>

      {/* Navigation */}
      <nav className="border-b border-white/10 bg-black/10">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex gap-1 overflow-x-auto">
            {[
              { id: 'overview', label: '📋 Обзор', icon: '' },
              { id: 'structure', label: '📁 Структура', icon: '' },
              { id: 'models', label: '🗃️ Модели', icon: '' },
              { id: 'views', label: '🔧 Представления', icon: '' },
              { id: 'templates', label: '🎨 Шаблоны', icon: '' },
              { id: 'install', label: '🚀 Установка', icon: '' },
            ].map(tab => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-5 py-4 text-sm font-medium whitespace-nowrap transition-all border-b-2 ${
                  activeTab === tab.id
                    ? 'border-blue-400 text-blue-300 bg-white/5'
                    : 'border-transparent text-gray-400 hover:text-white hover:bg-white/5'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Content */}
      <main className="max-w-7xl mx-auto px-6 py-10">
        {activeTab === 'overview' && <OverviewTab />}
        {activeTab === 'structure' && <StructureTab />}
        {activeTab === 'models' && <ModelsTab />}
        {activeTab === 'views' && <ViewsTab />}
        {activeTab === 'templates' && <TemplatesTab />}
        {activeTab === 'install' && <InstallTab />}
      </main>

      {/* Footer */}
      <footer className="border-t border-white/10 bg-black/20 py-6">
        <div className="max-w-7xl mx-auto px-6 text-center text-gray-400">
          <p>ShopMart © 2024 | Django 4.2 + Bootstrap 5.3 + AJAX</p>
        </div>
      </footer>
    </div>
  )
}

function OverviewTab() {
  return (
    <div className="space-y-8">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <StatCard icon="🗃️" title="6 Моделей" description="Category, Product, Cart, CartItem, Order, OrderItem" />
        <StatCard icon="🔧" title="15 Представлений" description="Включая AJAX-эндпоинты для корзины и поиска" />
        <StatCard icon="🎨" title="8 Шаблонов" description="Адаптивный дизайн на Bootstrap 5" />
      </div>

      <div className="bg-white/5 backdrop-blur-sm rounded-2xl border border-white/10 p-8">
        <h2 className="text-2xl font-bold text-white mb-4">🛒 О проекте</h2>
        <p className="text-gray-300 leading-relaxed mb-4">
          ShopMart — полнофункциональный интернет-магазин, разработанный на Django с использованием 
          Bootstrap 5 для фронтенда и AJAX для динамического взаимодействия без перезагрузки страниц.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
          <div>
            <h3 className="text-lg font-semibold text-blue-300 mb-3">✨ Функционал</h3>
            <ul className="space-y-2 text-gray-300">
              <li className="flex items-center gap-2"><span className="text-green-400">✓</span> Каталог товаров с фильтрацией и сортировкой</li>
              <li className="flex items-center gap-2"><span className="text-green-400">✓</span> Корзина с AJAX-обновлением</li>
              <li className="flex items-center gap-2"><span className="text-green-400">✓</span> Оформление заказа через AJAX</li>
              <li className="flex items-center gap-2"><span className="text-green-400">✓</span> Поиск товаров в реальном времени</li>
              <li className="flex items-center gap-2"><span className="text-green-400">✓</span> История заказов</li>
              <li className="flex items-center gap-2"><span className="text-green-400">✓</span> Админ-панель Django</li>
              <li className="flex items-center gap-2"><span className="text-green-400">✓</span> Адаптивный дизайн</li>
              <li className="flex items-center gap-2"><span className="text-green-400">✓</span> Скрипт заполнения БД</li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold text-purple-300 mb-3">🛠️ Технологии</h3>
            <ul className="space-y-2 text-gray-300">
              <li className="flex items-center gap-2"><span className="text-yellow-400">●</span> Python 3.10+ / Django 4.2</li>
              <li className="flex items-center gap-2"><span className="text-purple-400">●</span> Bootstrap 5.3</li>
              <li className="flex items-center gap-2"><span className="text-orange-400">●</span> AJAX (Fetch API)</li>
              <li className="flex items-center gap-2"><span className="text-blue-400">●</span> Bootstrap Icons</li>
              <li className="flex items-center gap-2"><span className="text-green-400">●</span> SQLite (по умолчанию)</li>
              <li className="flex items-center gap-2"><span className="text-red-400">●</span> Pillow (для изображений)</li>
              <li className="flex items-center gap-2"><span className="text-cyan-400">●</span> CSRF защита</li>
              <li className="flex items-center gap-2"><span className="text-pink-400">●</span> Session-based корзина</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

function StructureTab() {
  return (
    <div className="bg-white/5 backdrop-blur-sm rounded-2xl border border-white/10 p-8">
      <h2 className="text-2xl font-bold text-white mb-6">📁 Структура проекта</h2>
      <pre className="text-sm text-gray-300 font-mono overflow-x-auto bg-black/30 rounded-xl p-6 border border-white/5">
{`django_shop/
├── manage.py                 # Точка входа Django
├── requirements.txt          # Зависимости проекта
├── populate_shop.py          # Скрипт заполнения БД
├── config/                   # Настройки проекта
│   ├── __init__.py
│   ├── settings.py           # Основные настройки
│   ├── urls.py               # Корневые URL
│   ├── wsgi.py               # WSGI конфигурация
│   └── admin.py              # Настройки админки
├── shop/                     # Приложение магазина
│   ├── __init__.py
│   ├── admin.py              # Регистрация моделей в админке
│   ├── apps.py               # Конфигурация приложения
│   ├── context_processors.py # Контекст-процессор корзины
│   ├── forms.py              # Формы (OrderForm)
│   ├── models.py             # 6 моделей данных
│   ├── urls.py               # URL-маршруты (15 views)
│   └── views.py              # 15 представлений
├── templates/                # HTML шаблоны (8 шт.)
│   ├── base.html             # Базовый шаблон
│   ├── index.html            # Главная страница
│   ├── product_list.html     # Каталог товаров
│   ├── product_detail.html   # Страница товара
│   ├── category.html         # Товары по категории
│   ├── cart.html             # Корзина
│   ├── checkout.html         # Оформление заказа
│   ├── order_success.html    # Успешный заказ
│   ├── user_orders.html      # История заказов
│   └── order_detail.html     # Детали заказа
├── static/                   # Статические файлы
│   ├── css/
│   └── js/
└── media/                    # Загруженные файлы`}
      </pre>
    </div>
  )
}

function ModelsTab() {
  const models = [
    {
      name: 'Category',
      desc: 'Категория товаров',
      fields: ['name (CharField)', 'slug (SlugField)', 'description (TextField)', 'image (ImageField)', 'created_at (DateTimeField)'],
    },
    {
      name: 'Product',
      desc: 'Товар',
      fields: ['name (CharField)', 'slug (SlugField)', 'category (ForeignKey → Category)', 'description (TextField)', 'price (DecimalField)', 'old_price (DecimalField, nullable)', 'image (ImageField)', 'stock (PositiveIntegerField)', 'available (BooleanField)', 'created_at (DateTimeField)', 'updated_at (DateTimeField)'],
    },
    {
      name: 'Cart',
      desc: 'Корзина (привязана к сессии)',
      fields: ['session_key (CharField)', 'created_at (DateTimeField)', 'updated_at (DateTimeField)'],
    },
    {
      name: 'CartItem',
      desc: 'Элемент корзины',
      fields: ['cart (ForeignKey → Cart)', 'product (ForeignKey → Product)', 'quantity (PositiveIntegerField)', 'added_at (DateTimeField)'],
    },
    {
      name: 'Order',
      desc: 'Заказ',
      fields: ['first_name, last_name, email, phone (CharField)', 'address, city, postal_code (CharField)', 'status (CharField: pending/processing/shipped/delivered/cancelled)', 'total_price (DecimalField)', 'created_at, updated_at (DateTimeField)'],
    },
    {
      name: 'OrderItem',
      desc: 'Элемент заказа',
      fields: ['order (ForeignKey → Order)', 'product (ForeignKey → Product)', 'price (DecimalField)', 'quantity (PositiveIntegerField)'],
    },
  ]

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white mb-6">🗃️ Модели данных (6 моделей)</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {models.map((model, i) => (
          <div key={i} className="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 p-6">
            <div className="flex items-center gap-3 mb-3">
              <span className="w-8 h-8 bg-blue-500/20 rounded-lg flex items-center justify-center text-blue-300 font-bold text-sm">
                {i + 1}
              </span>
              <h3 className="text-xl font-bold text-white">{model.name}</h3>
            </div>
            <p className="text-purple-300 text-sm mb-3">{model.desc}</p>
            <ul className="space-y-1">
              {model.fields.map((field, j) => (
                <li key={j} className="text-gray-400 text-sm font-mono flex items-center gap-2">
                  <span className="text-green-400 text-xs">▸</span> {field}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  )
}

function ViewsTab() {
  const views = [
    { num: 1, name: 'home', url: '/', type: 'page', desc: 'Главная страница' },
    { num: 2, name: 'product_list', url: '/products/', type: 'page', desc: 'Каталог товаров с фильтрацией' },
    { num: 3, name: 'product_detail', url: '/product/<slug>/', type: 'page', desc: 'Детальная страница товара' },
    { num: 4, name: 'category_products', url: '/category/<slug>/', type: 'page', desc: 'Товары по категории' },
    { num: 5, name: 'view_cart', url: '/cart/', type: 'page', desc: 'Страница корзины' },
    { num: 6, name: 'add_to_cart', url: '/cart/add/', type: 'ajax', desc: 'AJAX: Добавить в корзину' },
    { num: 7, name: 'update_cart_item', url: '/cart/update/', type: 'ajax', desc: 'AJAX: Обновить количество' },
    { num: 8, name: 'remove_from_cart', url: '/cart/remove/', type: 'ajax', desc: 'AJAX: Удалить из корзины' },
    { num: 9, name: 'checkout', url: '/checkout/', type: 'page', desc: 'Страница оформления заказа' },
    { num: 10, name: 'process_order', url: '/checkout/process/', type: 'ajax', desc: 'AJAX: Обработка заказа' },
    { num: 11, name: 'order_success', url: '/order-success/<id>/', type: 'page', desc: 'Страница успешного заказа' },
    { num: 12, name: 'search_products', url: '/search/', type: 'ajax', desc: 'AJAX: Поиск товаров' },
    { num: 13, name: 'user_orders', url: '/orders/', type: 'page', desc: 'История заказов' },
    { num: 14, name: 'order_detail', url: '/order/<id>/', type: 'page', desc: 'Детали заказа' },
    { num: 15, name: 'api_cart_count', url: '/api/cart-count/', type: 'ajax', desc: 'AJAX: Количество в корзине' },
  ]

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white mb-6">🔧 Представления (15 views)</h2>
      <div className="bg-white/5 backdrop-blur-sm rounded-2xl border border-white/10 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b border-white/10 bg-white/5">
                <th className="text-left px-6 py-4 text-sm font-semibold text-gray-300">#</th>
                <th className="text-left px-6 py-4 text-sm font-semibold text-gray-300">View</th>
                <th className="text-left px-6 py-4 text-sm font-semibold text-gray-300">URL</th>
                <th className="text-left px-6 py-4 text-sm font-semibold text-gray-300">Тип</th>
                <th className="text-left px-6 py-4 text-sm font-semibold text-gray-300">Описание</th>
              </tr>
            </thead>
            <tbody>
              {views.map(view => (
                <tr key={view.num} className="border-b border-white/5 hover:bg-white/5 transition-colors">
                  <td className="px-6 py-3 text-gray-400">{view.num}</td>
                  <td className="px-6 py-3">
                    <code className="text-blue-300 bg-blue-500/10 px-2 py-1 rounded text-sm">{view.name}</code>
                  </td>
                  <td className="px-6 py-3">
                    <code className="text-gray-400 text-sm">{view.url}</code>
                  </td>
                  <td className="px-6 py-3">
                    {view.type === 'ajax' ? (
                      <span className="px-2 py-1 bg-orange-500/20 text-orange-300 rounded text-xs font-medium">AJAX</span>
                    ) : (
                      <span className="px-2 py-1 bg-green-500/20 text-green-300 rounded text-xs font-medium">Page</span>
                    )}
                  </td>
                  <td className="px-6 py-3 text-gray-300 text-sm">{view.desc}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}

function TemplatesTab() {
  const templates = [
    { name: 'base.html', desc: 'Базовый шаблон с навигацией, поиском, корзиной и подвалом', features: ['Bootstrap 5 CDN', 'Bootstrap Icons', 'AJAX поиск', 'CSRF защита', 'Toast уведомления'] },
    { name: 'index.html', desc: 'Главная страница с героем, категориями, скидками и популярными товарами', features: ['Hero секция', 'Карточки категорий', 'Товары со скидкой', 'Блок преимуществ'] },
    { name: 'product_list.html', desc: 'Каталог товаров с боковой панелью фильтров и сортировкой', features: ['Фильтр по цене', 'Сортировка', 'Карточки товаров', 'Адаптивная сетка'] },
    { name: 'product_detail.html', desc: 'Детальная страница товара с описанием и похожими товарами', features: ['Галерея', 'Выбор количества', 'Похожие товары', 'Хлебные крошки'] },
    { name: 'category.html', desc: 'Страница товаров выбранной категории', features: ['Описание категории', 'Сетка товаров', 'Бейджи скидок'] },
    { name: 'cart.html', desc: 'Страница корзины с AJAX-обновлением', features: ['Изменение количества', 'Удаление товаров', 'Итоговая сумма', 'AJAX без перезагрузки'] },
    { name: 'checkout.html', desc: 'Форма оформления заказа с валидацией', features: ['Форма доставки', 'Сводка заказа', 'AJAX отправка', 'Валидация полей'] },
    { name: 'order_success.html', desc: 'Страница подтверждения успешного заказа', features: ['Детали заказа', 'Анимация успеха', 'Ссылки навигации'] },
  ]

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white mb-6">🎨 Шаблоны (8 + 2 дополнительных)</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {templates.map((tmpl, i) => (
          <div key={i} className="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 p-6">
            <div className="flex items-center gap-3 mb-3">
              <span className="text-2xl">📄</span>
              <h3 className="text-lg font-bold text-white font-mono">{tmpl.name}</h3>
            </div>
            <p className="text-gray-300 text-sm mb-3">{tmpl.desc}</p>
            <div className="flex flex-wrap gap-2">
              {tmpl.features.map((f, j) => (
                <span key={j} className="px-2 py-1 bg-purple-500/10 text-purple-300 rounded text-xs">
                  {f}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

function InstallTab() {
  const steps = [
    {
      title: '1. Создать виртуальное окружение',
      code: 'python -m venv venv',
      note: 'Для Windows: python -m venv venv',
    },
    {
      title: '2. Активировать виртуальное окружение',
      code: 'source venv/bin/activate  # Linux/Mac\nvenv\\Scripts\\activate     # Windows',
      note: '',
    },
    {
      title: '3. Установить зависимости',
      code: 'pip install -r requirements.txt',
      note: 'Установит Django, Pillow и другие зависимости',
    },
    {
      title: '4. Выполнить миграции',
      code: 'python manage.py makemigrations\npython manage.py migrate',
      note: 'Создаст таблицы в базе данных SQLite',
    },
    {
      title: '5. Заполнить базу данных',
      code: 'python populate_shop.py',
      note: 'Создаст категории, товары и суперпользователя (admin/admin123)',
    },
    {
      title: '6. Запустить сервер',
      code: 'python manage.py runserver',
      note: 'Сервер будет доступен по адресу http://127.0.0.1:8000/',
    },
  ]

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-white mb-6">🚀 Инструкция по запуску</h2>
      
      <div className="bg-yellow-500/10 border border-yellow-500/30 rounded-xl p-6">
        <h3 className="text-yellow-300 font-semibold mb-2">⚠️ Требования</h3>
        <ul className="text-gray-300 text-sm space-y-1">
          <li>• Python 3.10 или выше</li>
          <li>• pip (менеджер пакетов Python)</li>
          <li>• Перейдите в папку django_shop/ перед выполнением команд</li>
        </ul>
      </div>

      <div className="space-y-4">
        {steps.map((step, i) => (
          <div key={i} className="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 p-6">
            <h3 className="text-lg font-semibold text-white mb-3">{step.title}</h3>
            <pre className="bg-black/40 rounded-lg p-4 text-sm font-mono text-green-300 overflow-x-auto border border-white/5">
              {step.code}
            </pre>
            {step.note && (
              <p className="text-gray-400 text-sm mt-2 italic">{step.note}</p>
            )}
          </div>
        ))}
      </div>

      <div className="bg-green-500/10 border border-green-500/30 rounded-xl p-6">
        <h3 className="text-green-300 font-semibold mb-3">✅ После запуска</h3>
        <ul className="text-gray-300 space-y-2">
          <li>🌐 <strong>Сайт:</strong> <code className="text-blue-300">http://127.0.0.1:8000/</code></li>
          <li>🔧 <strong>Админ-панель:</strong> <code className="text-blue-300">http://127.0.0.1:8000/admin/</code></li>
          <li>👤 <strong>Логин:</strong> admin / admin123</li>
        </ul>
      </div>

      <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-6">
        <h3 className="text-blue-300 font-semibold mb-3">📦 Быстрый старт (все команды)</h3>
        <pre className="bg-black/40 rounded-lg p-4 text-sm font-mono text-green-300 overflow-x-auto border border-white/5">
{`cd django_shop
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\\Scripts\\activate       # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python populate_shop.py
python manage.py runserver`}
        </pre>
      </div>
    </div>
  )
}

function StatCard({ icon, title, description }: { icon: string; title: string; description: string }) {
  return (
    <div className="bg-white/5 backdrop-blur-sm rounded-xl border border-white/10 p-6 text-center">
      <div className="text-4xl mb-3">{icon}</div>
      <h3 className="text-xl font-bold text-white mb-2">{title}</h3>
      <p className="text-gray-400 text-sm">{description}</p>
    </div>
  )
}

export default App
