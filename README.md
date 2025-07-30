# 🍎 E-commerce API with Django, PostgreSQL, JWT Auth, and WebSockets

This is a fully functional backend API for an e-commerce application built with Django and Django REST Framework. It supports user registration, JWT login, product/category management, order creation, and real-time order status updates using Django Channels + WebSockets.

---

## ✨ Features

✅ User Registration & Login (JWT)
✅ Authenticated User Profile (view/update)
✅ Category Management
✅ Product Management with Price, Stock, Category
✅ Product Filtering (min/max price, in-stock, category)
✅ Order Placement with Total Calculation
✅ Order Status Updates (`PENDING`, `SHIPPED`, `DELIVERED`)
✅ Real-time WebSocket Notification on Status Update
✅ Redis-powered Django Channels
✅ PostgreSQL as DB backend

---

## 🛠️ Tech Stack

* **Backend**: Django, DRF, Django Channels
* **Auth**: JWT (SimpleJWT)
* **DB**: PostgreSQL
* **Real-time**: WebSockets (Channels + Redis)
* **Tools**: Postman, Redis, Daphne

---

## 🧑‍💻 Setup Instructions

### 1. Clone & Setup Virtual Env

```bash
git clone https://github.com/vikas010203/ecommerce-api.git
cd ecommerce-api
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup PostgreSQL (or SQLite for testing)

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Or use SQLite for testing:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 4. Run Migrations & Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start Redis Server

Make sure Redis is running:

```bash
redis-server
```

### 6. Start Development Server

```bash
daphne ecommerce_api.asgi:application
```

---

## 🔌 API Endpoints

| Endpoint                   | Method | Description                     |
| -------------------------- | ------ | ------------------------------- |
| `/api/register/`           | POST   | Register a new user             |
| `/api/login/`              | POST   | JWT login                       |
| `/api/profile/`            | GET    | View authenticated profile      |
| `/api/categories/`         | GET    | List all categories             |
| `/api/products/`           | GET    | List all products (filterable)  |
| `/api/orders/create/`      | POST   | Create a new order              |
| `/api/orders/`             | GET    | View user orders                |
| `/api/orders/<id>/update/` | PUT    | Update order status             |
| `/ws/orders/<id>/`         | WS     | WebSocket for real-time updates |

---

## 🔀 Real-time Notifications

* WebSocket clients subscribe to `/ws/orders/<order_id>/`
* When order status is updated via REST API, a real-time event is broadcasted via WebSocket
* Powered by **Django Channels** and **Redis**

---

## 📂 Project Structure

```
ecommerce_api/
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── consumers.py
│   └── routing.py
├── ecommerce_api/
│   ├── asgi.py
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📦 Deployment Notes

* Use **Gunicorn + Daphne** or **Uvicorn** for production.
* Configure **Redis** on a persistent server (like AWS ElastiCache or Docker Redis).
* Secure credentials using **`.env`** file and **`django-environ`**.

---

## ✨ Author

* GitHub: [@vikas010203](https://github.com/vikas010203)

---

## 📜 License

This project is licensed under the MIT License.

---
