import streamlit as st

from food_delivery import (
    Customer,
    DeliveryPartner,
    MenuItem,
    Restaurant,
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Smart Food Corner",
    page_icon="🍔",
    layout="wide",
)


# ============================================================
# SESSION STATE
# ============================================================

if "customer" not in st.session_state:
    st.session_state.customer = None

if "delivery_partner" not in st.session_state:
    st.session_state.delivery_partner = None

if "order" not in st.session_state:
    st.session_state.order = None


# ============================================================
# RESTAURANT
# ============================================================

if "restaurant" not in st.session_state:

    restaurant = Restaurant(
        "Food Corner",
        "Sambhajinagar"
    )

    restaurant.add_item(
        MenuItem("Veg Burger", 120, True)
    )

    restaurant.add_item(
        MenuItem("Pizza", 250, True)
    )

    restaurant.add_item(
        MenuItem("Paneer Wrap", 150, True)
    )

    restaurant.add_item(
        MenuItem("Chicken Biryani", 220, False)
    )

    restaurant.add_item(
        MenuItem("French Fries", 100, True)
    )

    st.session_state.restaurant = restaurant


restaurant = st.session_state.restaurant


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🍔 Smart Food Corner")

    st.caption(
        "Food Ordering & Restaurant Analytics"
    )

    st.divider()

    st.subheader("Navigation")

    st.write("🏠 Dashboard")
    st.write("👤 Customer")
    st.write("🍽️ Menu")
    st.write("🛒 Orders")
    st.write("🛵 Delivery")
    st.write("📊 Analytics")

    st.divider()

    st.subheader("Technology")

    st.write("🐍 Python")
    st.write("🧩 OOP")
    st.write("🎨 Streamlit")

    st.divider()

    st.caption(
        "Portfolio Project"
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🍔 Smart Food Corner")

st.subheader(
    "Food Ordering & Restaurant Analytics"
)

st.write(
    "A smart food ordering application that combines "
    "customer management, order tracking, delivery "
    "operations and restaurant insights."
)


st.divider()


# ============================================================
# DASHBOARD
# ============================================================

st.header("🏠 Dashboard")

st.write(
    "Welcome! Here's a quick overview of the application."
)


# ============================================================
# DASHBOARD METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


# Customer
with col1:

    if st.session_state.customer:

        st.metric(
            "👤 Customer",
            st.session_state.customer._name
        )

    else:

        st.metric(
            "👤 Customer",
            "Not Created"
        )


# Wallet
with col2:

    if st.session_state.customer:

        st.metric(
            "💰 Wallet",
            f"₹{st.session_state.customer._wallet_balance:.0f}"
        )

    else:

        st.metric(
            "💰 Wallet",
            "₹0"
        )


# Order
with col3:

    if st.session_state.order:

        st.metric(
            "📦 Order",
            st.session_state.order._status
        )

    else:

        st.metric(
            "📦 Order",
            "No Order"
        )


# Delivery Partner
with col4:

    if st.session_state.delivery_partner:

        if st.session_state.delivery_partner.is_available:

            status = "Available"

        else:

            status = "Busy"

        st.metric(
            "🛵 Partner",
            status
        )

    else:

        st.metric(
            "🛵 Partner",
            "Not Created"
        )


st.divider()


# ============================================================
# APPLICATION MODULES
# ============================================================

st.header("✨ Explore the Application")


col1, col2, col3 = st.columns(3)


with col1:

    st.subheader("👤 Customer")

    st.write(
        "Create a customer profile, "
        "manage wallet balance and "
        "track order history."
    )


with col2:

    st.subheader("🍽️ Food Ordering")

    st.write(
        "Browse the restaurant menu, "
        "select food items and place orders."
    )


with col3:

    st.subheader("🛵 Delivery")

    st.write(
        "Assign delivery partners, "
        "accept orders and complete "
        "delivery using OTP verification."
    )


st.divider()


# ============================================================
# RESTAURANT INFORMATION
# ============================================================

st.header("🍽️ Restaurant")

restaurant_col1, restaurant_col2 = st.columns(2)


with restaurant_col1:

    st.subheader(
        restaurant.name
    )

    st.write(
        f"📍 {restaurant.location}"
    )


with restaurant_col2:

    st.metric(
        "Menu Items",
        len(restaurant.get_menu())
    )


st.divider()


# ============================================================
# CURRENT ORDER
# ============================================================

st.header("📦 Current Order")

if st.session_state.order:

    order = st.session_state.order

    order_col1, order_col2, order_col3 = st.columns(3)

    with order_col1:

        st.metric(
            "Order ID",
            order._order_id
        )

    with order_col2:

        st.metric(
            "Status",
            order._status
        )

    with order_col3:

        st.metric(
            "Bill",
            f"₹{order.calculate_bill():.2f}"
        )

else:

    st.info(
        "No order has been placed yet."
    )


st.divider()


# ============================================================
# QUICK START
# ============================================================

st.header("🚀 Quick Start")

st.write(
    "To use the application:"
)

st.write(
    "1. Create a customer"
)

st.write(
    "2. Add money to the wallet"
)

st.write(
    "3. Browse the menu"
)

st.write(
    "4. Place an order"
)

st.write(
    "5. Create a delivery partner"
)

st.write(
    "6. Accept the order"
)

st.write(
    "7. Verify the OTP"
)

st.write(
    "8. Complete the delivery"
)


st.divider()


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "🍔 Smart Food Corner • "
    "Python OOP + Streamlit • Portfolio Project"
)
