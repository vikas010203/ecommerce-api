# 🛒 E-commerce API with Django, PostgreSQL, JWT Auth, and WebSockets

This is a fully functional backend API for an e-commerce application built with Django and Django REST Framework. It supports user registration, JWT login, product/category management, order creation, and real-time order status updates using Django Channels + WebSockets.

---

## 🚀 Features

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

- **Backend**: Django, DRF, Django Channels
- **Auth**: JWT (SimpleJWT)
- **DB**: PostgreSQL
- **Real-time**: WebSockets (Channels + Redis)
- **Tools**: Postman, Redis, Daphne

---

## 🧑‍💻 Setup Instructions

### 1. Clone & Setup Virtual Env

```bash
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
