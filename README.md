# 🍔 Food Delivery System

### Object-Oriented Python Application with an Interactive Streamlit Interface

A practical **Food Delivery Management System** developed using **Python Object-Oriented Programming (OOP)** and **Streamlit**.

The project demonstrates how core OOP concepts can be applied to a real-world food delivery workflow — from creating a customer and managing a wallet to placing an order, assigning a delivery partner, verifying an OTP, and completing delivery.

---

## 🚀 Live Demo

### 🍔 [Launch the Food Delivery Application](https://food-delivery-egdhbbo89ebaejcxiebmpn.streamlit.app/)

> **Try the application directly in your browser.**

---

## 📌 Project Overview

The Food Delivery System models the core components of a simplified online food-ordering platform.

The application contains separate classes for:

- 👤 Users
- 🧑‍💼 Customers
- 🛵 Delivery Partners
- 🏪 Restaurants
- 🍽️ Menu Items
- 📦 Orders

The underlying business logic is implemented using Python classes, while **Streamlit provides an interactive web interface** for performing the complete order and delivery workflow.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 👤 **Customer Management** | Create customers with name, phone and address |
| 💰 **Wallet Management** | Add funds and display wallet balance |
| 🏪 **Restaurant Menu** | View restaurant information and available food items |
| 🍽️ **Food Selection** | Select multiple items from the menu |
| 🛒 **Order Placement** | Create an order and generate an Order ID |
| 🧾 **Automatic Billing** | Calculate subtotal, GST and packaging charges |
| 🛵 **Delivery Partner** | Create and manage delivery partner information |
| ✅ **Order Acceptance** | Delivery partner accepts the order |
| 🔐 **OTP Verification** | Verify OTP before completing delivery |
| 📦 **Order Tracking** | Track order status throughout the workflow |
| 🌐 **Streamlit UI** | Interactive browser-based application |

---

## 🔄 Application Workflow

```text
        👤 Create Customer
                │
                ▼
        💰 Add Wallet Balance
                │
                ▼
        🍽️ View Restaurant Menu
                │
                ▼
        🛒 Select Food Items
                │
                ▼
          📦 Place Order
                │
                ▼
       🛵 Create Delivery Partner
                │
                ▼
          ✅ Accept Order
                │
                ▼
          🔐 Enter OTP
                │
                ▼
       🎉 Complete Delivery
```

### Order Lifecycle

```text
Placed  →  Accepted  →  Delivered
```

An incorrect OTP keeps the order in the accepted state until the correct OTP is provided. This matches the project's intended order lifecycle.

---

# 🧠 Object-Oriented Programming

The project focuses on applying important OOP principles to a practical use case.

### 1. Abstraction

`User` is designed as an abstract base class with abstract methods such as:

```python
notify()
display_profile()
```

This provides a common structure for different types of users.

### 2. Inheritance

The following classes inherit from `User`:

```text
User
 ├── Customer
 └── DeliveryPartner
```

This allows common user functionality, such as wallet management, to be reused.

### 3. Encapsulation

Internal application state is represented using attributes such as:

```text
_wallet_balance
_menu
_status
_otp
```

This keeps implementation details separated from the public interface.

### 4. Polymorphism

`Customer` and `DeliveryPartner` provide their own implementations of common user behaviour such as `notify()` and `display_profile()`.

### 5. Composition

The system uses relationships between objects:

```text
Restaurant
   └── MenuItem

Order
   └── MenuItem

Customer
   └── Order

DeliveryPartner
   └── Order
```

These concepts are also reflected in the architecture documented in the original project.

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │      Streamlit UI       │
                    │        app.py            │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Food Delivery OOP    │
                    │    food_delivery.py     │
                    └────────────┬────────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
             ▼                   ▼                   ▼
        👤 Customer         🏪 Restaurant      🛵 Delivery
             │                   │                   │
             │                   ▼                   │
             │              🍽️ Menu Items           │
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 ▼
                           📦 Order
                                 │
                                 ▼
                           🔐 OTP Check
                                 │
                                 ▼
                           🎉 Delivered
```

---

# 💰 Billing Logic

The order bill is calculated using:

```text
Total Bill
    =
Subtotal
+ 5% GST
+ ₹20 Packaging Fee
```

For example:

```text
Subtotal       ₹430.00
GST (5%)        ₹21.50
Packaging       ₹20.00
──────────────────────
Total           ₹471.50
```

The project currently uses a fixed estimated delivery time of **30 minutes**.

---

# 🖥️ Streamlit Application

The Streamlit interface provides an interactive way to work with the OOP classes.

### Main sections

```text
1. Create Customer
2. Add Wallet Balance
3. Restaurant Menu
4. Place Order
5. Order Status
6. Create Delivery Partner
7. Accept Order
8. Enter OTP & Complete Delivery
9. Delivery Summary
```

The application uses Streamlit session state to preserve customer, restaurant, order and delivery-partner information while interacting with the interface.

---

# 📂 Project Structure

```text
Food-Delivery/
│
├── app.py
│   └── Streamlit application
│
├── food_delivery.py
│   └── Core OOP classes and business logic
│
├── streamlit_app.py
│   └── Streamlit implementation/reference
│
├── Food_Delivery_System_Notebook.ipynb
│   └── Project development notebook
│
├── .devcontainer/
│   └── Development environment configuration
│
└── README.md
    └── Project documentation
```

---

# 🛠️ Tech Stack

### Programming

- 🐍 Python

### Framework

- 🎈 Streamlit

### Core Concepts

- Object-Oriented Programming
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism
- Composition
- Session State

### Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# ⚙️ Run Locally

## 1. Clone the Repository

```bash
git clone https://github.com/shwetavanarse/Food-Delivery.git
```

## 2. Open the Project

```bash
cd Food-Delivery
```

## 3. Install Streamlit

```bash
pip install streamlit
```

## 4. Run the Application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

# 🧪 Example User Journey

### 👤 Step 1 — Create Customer

Enter:

- Customer Name
- Phone
- Address

Then create the customer profile.

### 💰 Step 2 — Add Wallet Balance

Add money to the customer's wallet and view the updated balance.

### 🍽️ Step 3 — Explore Restaurant Menu

View:

- Food item
- Price
- Veg / Non-Veg classification

### 🛒 Step 4 — Place Order

Select one or more food items.

The application calculates:

```text
Subtotal
+ GST
+ Packaging Fee
= Total Bill
```

### 🛵 Step 5 — Create Delivery Partner

Enter:

- Partner Name
- Phone
- Vehicle

### ✅ Step 6 — Accept Order

The delivery partner accepts the placed order.

### 🔐 Step 7 — Verify OTP

Enter the delivery OTP.

### 🎉 Step 8 — Complete Delivery

After successful verification, the order is marked as delivered and the final order summary is displayed.

---

# 📚 Learning Outcomes

This project provided practical experience in:

- Designing real-world classes and objects
- Applying abstraction and inheritance
- Implementing polymorphism
- Encapsulating application state
- Working with object relationships
- Building a multi-step application workflow
- Managing state using Streamlit
- Creating interactive Python web applications
- Organizing a project using Git and GitHub
- Connecting Python OOP logic with a user interface

---

# 🔮 Future Enhancements

Potential improvements include:

- 💳 Payment processing
- 🗄️ Database integration
- 🔐 User authentication
- 🏪 Multiple restaurants
- 🔎 Food and restaurant search
- ⭐ Customer ratings and reviews
- 📍 Real-time delivery tracking
- 📊 Admin dashboard
- 🧾 Invoice generation
- 📧 Order notifications
- 🔢 Unique OTP generation for every order
- 🧪 Automated unit testing
- 🛵 Intelligent delivery-partner assignment

These are intentionally listed as future enhancements rather than current features. The original project also identifies improvements such as wallet deduction, restaurant-menu validation, unique OTPs, partner assignment, Streamlit integration and unit testing.

---

# 🎯 Project Highlights

> **A practical demonstration of Python Object-Oriented Programming concepts through a real-world food delivery workflow, enhanced with an interactive Streamlit application.**

### Core Workflow

**Customer → Restaurant → Order → Delivery Partner → OTP Verification → Delivery**

---

# 👩‍💻 Author

## Shweta Vanarse

**BCA (Science) Graduate | Data Analytics | Python | SQL | Power BI**

📍 Chhatrapati Sambhajinagar, Maharashtra, India

### Connect with me

- 💻 **GitHub:** [shwetavanarse](https://github.com/shwetavanarse)
- 🔗 **LinkedIn:** [Shweta Vanarse](https://www.linkedin.com/in/shweta-vanarse-aa82313b1/)

---

## ⭐ Support

If you found this project interesting, consider giving the repository a ⭐ on GitHub.

---

### Built with

**🐍 Python · 🎈 Streamlit · 🧠 OOP · 📓 Jupyter · 🐙 GitHub**
