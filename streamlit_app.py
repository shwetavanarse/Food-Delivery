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


# IMPORTANT
restaurant = st.session_state.restaurant


# ============================================================
# RESTAURANT
# ============================================================

# ============================================================
# RESTAURANT MENU
# ============================================================

st.header("🍽️ Our Menu")

st.write(
    f"**{restaurant.name}** • 📍 {restaurant.location}"
)

st.caption(
    "Choose from our freshly available menu items."
)

st.divider()


# ------------------------------------------------------------
# MENU ITEMS
# ------------------------------------------------------------

menu_items = restaurant.get_menu()

# Display 3 food cards per row
for i in range(0, len(menu_items), 3):

    cols = st.columns(3)

    for j, col in enumerate(cols):

        index = i + j

        if index >= len(menu_items):
            break

        item = menu_items[index]

        with col:

            # Food emoji based on item name
            food_icons = {
                "Veg Burger": "🍔",
                "Pizza": "🍕",
                "Paneer Wrap": "🌯",
                "Chicken Biryani": "🍗",
                "French Fries": "🍟"
            }

            icon = food_icons.get(
                item.name,
                "🍽️"
            )

            st.subheader(
                f"{icon} {item.name}"
            )

            st.write(
                f"### ₹{item.price:.0f}"
            )

            if item.is_veg:

                st.success(
                    "🟢 Vegetarian"
                )

            else:

                st.error(
                    "🔴 Non-Vegetarian"
                )

            st.write(
                "Freshly prepared and "
                "available for ordering."
            )


st.divider()


# ============================================================
# MENU SUMMARY
# ============================================================

st.subheader("📋 Menu Overview")

menu_col1, menu_col2, menu_col3 = st.columns(3)

with menu_col1:

    st.metric(
        "🍽️ Total Items",
        len(menu_items)
    )


with menu_col2:

    veg_count = sum(
        1
        for item in menu_items
        if item.is_veg
    )

    st.metric(
        "🟢 Vegetarian",
        veg_count
    )


with menu_col3:

    nonveg_count = sum(
        1
        for item in menu_items
        if not item.is_veg
    )

    st.metric(
        "🔴 Non-Vegetarian",
        nonveg_count
    )

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
# CUSTOMER & WALLET
# ============================================================

st.header("👤 Customer & Wallet")

customer_col1, customer_col2 = st.columns([1.4, 1])


# ------------------------------------------------------------
# CUSTOMER PROFILE
# ------------------------------------------------------------

with customer_col1:

    st.subheader("Create Customer Profile")

    with st.form("customer_form"):

        customer_name = st.text_input(
            "Full Name",
            placeholder="Enter customer name"
        )

        customer_phone = st.text_input(
            "Phone Number",
            placeholder="Enter phone number"
        )

        customer_address = st.text_input(
            "Delivery Address",
            placeholder="Enter delivery address"
        )

        create_customer = st.form_submit_button(
            "Create Customer",
            type="primary"
        )

        if create_customer:

            if (
                customer_name
                and customer_phone
                and customer_address
            ):

                st.session_state.customer = Customer(
                    customer_name,
                    customer_phone,
                    customer_address
                )

                st.success(
                    f"Welcome, {customer_name}! 🎉"
                )

            else:

                st.warning(
                    "Please fill in all customer details."
                )


# ------------------------------------------------------------
# CUSTOMER INFORMATION
# ------------------------------------------------------------

with customer_col2:

    st.subheader("Customer Overview")

    if st.session_state.customer:

        customer = st.session_state.customer

        st.write(
            f"**Name:** {customer._name}"
        )

        st.write(
            f"**Phone:** {customer._phone}"
        )

        st.write(
            f"**Address:** {customer.address}"
        )

        st.metric(
            "💰 Wallet Balance",
            f"₹{customer._wallet_balance:.2f}"
        )

    else:

        st.info(
            "No customer profile created yet."
        )


st.divider()


# ============================================================
# ADD WALLET BALANCE
# ============================================================

st.subheader("💰 Manage Wallet")

if st.session_state.customer:

    wallet_col1, wallet_col2 = st.columns([1, 2])

    with wallet_col1:

        wallet_amount = st.number_input(
            "Amount to Add (₹)",
            min_value=0.0,
            step=100.0,
            value=100.0
        )

    with wallet_col2:

        st.write("")
        st.write("")

        if st.button(
            "➕ Add Money",
            type="primary"
        ):

            if wallet_amount > 0:

                st.session_state.customer.add_to_wallet(
                    wallet_amount
                )

                st.success(
                    f"₹{wallet_amount:.2f} added to wallet!"
                )

            else:

                st.warning(
                    "Enter an amount greater than ₹0."
                )

else:

    st.info(
        "Create a customer profile first "
        "to manage the wallet."
    )
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
# SMART FOOD ORDERING
# ============================================================

st.header("🛒 Smart Food Ordering")

st.caption(
    "Select your favourite items and create your order."
)


# ------------------------------------------------------------
# CHECK CUSTOMER
# ------------------------------------------------------------

if st.session_state.customer is None:

    st.info(
        "👤 Please create a customer profile first "
        "before placing an order."
    )

else:

    customer = st.session_state.customer

    # --------------------------------------------------------
    # CUSTOMER ORDER INFO
    # --------------------------------------------------------

    order_info_col1, order_info_col2 = st.columns(2)

    with order_info_col1:

        st.info(
            f"👤 Ordering for **{customer._name}**"
        )

    with order_info_col2:

        st.info(
            f"💰 Wallet Balance: "
            f"**₹{customer._wallet_balance:.2f}**"
        )


    st.divider()


    # --------------------------------------------------------
    # FOOD SELECTION
    # --------------------------------------------------------

    st.subheader("🍽️ Select Food Items")

    item_names = [
        item.name
        for item in restaurant.get_menu()
    ]

    selected_items = st.multiselect(
        "Choose one or more items",
        item_names,
        placeholder="Select food items..."
    )


    # --------------------------------------------------------
    # BILL PREVIEW
    # --------------------------------------------------------

    if selected_items:

        selected_objects = [
            item
            for item in restaurant.get_menu()
            if item.name in selected_items
        ]

        subtotal = sum(
            item.price
            for item in selected_objects
        )

        gst = subtotal * 0.05

        packaging_fee = 20

        total = (
            subtotal
            + gst
            + packaging_fee
        )


        st.divider()

        st.subheader("🧾 Bill Summary")


        bill_col1, bill_col2 = st.columns(
            [2, 1]
        )


        with bill_col1:

            st.write("**Selected Items**")

            for item in selected_objects:

                icon = {
                    "Veg Burger": "🍔",
                    "Pizza": "🍕",
                    "Paneer Wrap": "🌯",
                    "Chicken Biryani": "🍗",
                    "French Fries": "🍟"
                }.get(
                    item.name,
                    "🍽️"
                )

                st.write(
                    f"{icon} {item.name} — "
                    f"₹{item.price:.2f}"
                )


        with bill_col2:

            st.metric(
                "Subtotal",
                f"₹{subtotal:.2f}"
            )

            st.metric(
                "GST (5%)",
                f"₹{gst:.2f}"
            )

            st.metric(
                "Packaging Fee",
                f"₹{packaging_fee:.2f}"
            )

            st.metric(
                "Total Amount",
                f"₹{total:.2f}"
            )


        st.divider()


        # ----------------------------------------------------
        # PLACE ORDER
        # ----------------------------------------------------

        if st.button(
            "🛒 Place Order",
            type="primary",
            use_container_width=True
        ):

            try:

                order = customer.place_order(
                    restaurant,
                    selected_objects
                )

                st.session_state.order = order

                st.success(
                    f"🎉 Order "
                    f"**{order._order_id}** "
                    f"placed successfully!"
                )

                st.info(
                    f"📦 Order Status: "
                    f"**{order._status}**"
                )

                st.warning(
                    f"🔐 Delivery OTP: "
                    f"**{order._otp}** "
                    f"(Demo purpose)"
                )

                st.rerun()


            except Exception as e:

                st.error(
                    f"Unable to place order: {e}"
                )


    else:

        st.info(
            "🍽️ Select at least one food item "
            "to see your bill."
        )


# ============================================================
# CURRENT ORDER
# ============================================================

st.divider()

st.header("📦 Current Order")

if st.session_state.order:

    order = st.session_state.order


    # --------------------------------------------------------
    # ORDER STATUS
    # --------------------------------------------------------

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
            "Total Bill",
            f"₹{order.calculate_bill():.2f}"
        )


    st.success(
        "Your order has been successfully created."
    )


else:

    st.info(
        "🛒 No order has been placed yet."
    )


# ============================================================
# DELIVERY OPERATIONS
# ============================================================

st.divider()

st.header("🛵 Delivery Operations")

st.caption(
    "Manage delivery partners, accept orders and complete "
    "deliveries using OTP verification."
)


# ============================================================
# CREATE DELIVERY PARTNER
# ============================================================

st.subheader("👤 Create Delivery Partner")

partner_col1, partner_col2, partner_col3 = st.columns(3)

with partner_col1:

    partner_name = st.text_input(
        "Partner Name",
        placeholder="Enter delivery partner name",
        key="partner_name"
    )

with partner_col2:

    partner_phone = st.text_input(
        "Partner Phone",
        placeholder="Enter phone number",
        key="partner_phone"
    )

with partner_col3:

    vehicle = st.selectbox(
        "Vehicle",
        [
            "Bike",
            "Scooter",
            "Car"
        ],
        key="partner_vehicle"
    )


if st.button(
    "🛵 Create Delivery Partner",
    type="primary",
    use_container_width=True
):

    if partner_name and partner_phone:

        st.session_state.delivery_partner = DeliveryPartner(
            partner_name,
            partner_phone,
            vehicle
        )

        st.success(
            f"🎉 Delivery partner "
            f"**{partner_name}** created successfully!"
        )

        st.rerun()

    else:

        st.warning(
            "Please enter the partner name and phone number."
        )


# ============================================================
# DELIVERY PARTNER STATUS
# ============================================================

st.divider()

st.subheader("📊 Partner Status")

if st.session_state.delivery_partner:

    partner = st.session_state.delivery_partner

    status_col1, status_col2, status_col3 = st.columns(3)

    with status_col1:

        st.metric(
            "👤 Partner",
            partner._name
        )

    with status_col2:

        if partner.is_available:

            st.metric(
                "🟢 Availability",
                "Available"
            )

        else:

            st.metric(
                "🔴 Availability",
                "Busy"
            )

    with status_col3:

        st.metric(
            "🛵 Vehicle",
            partner.vehicle
        )

else:

    st.info(
        "No delivery partner has been created yet."
    )


# ============================================================
# ACCEPT ORDER
# ============================================================

st.divider()

st.subheader("📦 Accept Order")

if st.session_state.order is None:

    st.info(
        "Place an order first before assigning a delivery partner."
    )

elif st.session_state.delivery_partner is None:

    st.info(
        "Create a delivery partner first."
    )

else:

    order = st.session_state.order
    partner = st.session_state.delivery_partner

    accept_col1, accept_col2 = st.columns(2)

    with accept_col1:

        st.write(
            f"**Order:** {order._order_id}"
        )

        st.write(
            f"**Current Status:** {order._status}"
        )

    with accept_col2:

        if partner.is_available:

            if st.button(
                "✅ Accept Order",
                type="primary",
                use_container_width=True
            ):

                partner.accept_order(order)

                st.success(
                    f"Order **{order._order_id}** "
                    f"accepted by {partner._name}."
                )

                st.rerun()

        else:

            st.warning(
                "This delivery partner is currently busy."
            )


# ============================================================
# COMPLETE DELIVERY
# ============================================================

st.divider()

st.subheader("🔐 Complete Delivery")

if st.session_state.order is None:

    st.info(
        "No order is available for delivery."
    )

elif st.session_state.delivery_partner is None:

    st.info(
        "Create a delivery partner first."
    )

else:

    order = st.session_state.order
    partner = st.session_state.delivery_partner

    if order._status == "Placed":

        st.warning(
            "⚠️ The order must be accepted by a delivery "
            "partner before it can be delivered."
        )

    elif order._status == "Accepted":

        st.info(
            "📍 Order is out for delivery. "
            "Enter the customer's OTP to complete delivery."
        )

        otp_col1, otp_col2 = st.columns([1, 2])

        with otp_col1:

            delivery_otp = st.number_input(
                "Enter 4-digit OTP",
                min_value=1000,
                max_value=9999,
                step=1,
                key="delivery_otp"
            )

        with otp_col2:

            st.write("")
            st.write("")

            if st.button(
                "🎉 Complete Delivery",
                type="primary",
                use_container_width=True
            ):

                partner.deliver(
                    order,
                    int(delivery_otp)
                )

                if order._status == "Delivered":

                    st.success(
                        f"🎉 Order **{order._order_id}** "
                        "delivered successfully!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "❌ Incorrect OTP. "
                        "Delivery could not be completed."
                    )

    elif order._status == "Delivered":

        st.success(
            f"🎉 Order **{order._order_id}** "
            "has already been delivered."
        )
    


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
