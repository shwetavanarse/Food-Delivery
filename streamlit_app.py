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
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f8f9fb;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #ff6b35,
            #ff8c42
        );
        color: white;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 17px;
        margin-bottom: 0;
    }

    .food-card {
        padding: 20px;
        border-radius: 18px;
        background: white;
        border: 1px solid #eeeeee;
        margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    .food-title {
        font-size: 21px;
        font-weight: 700;
    }

    .food-price {
        font-size: 20px;
        font-weight: 700;
        color: #ff6b35;
    }

    .status-card {
        padding: 18px;
        border-radius: 15px;
        background: white;
        border: 1px solid #eeeeee;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .small-text {
        color: #666666;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
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


restaurant = st.session_state.restaurant


# ============================================================
# FOOD ICONS
# ============================================================

food_icons = {
    "Veg Burger": "🍔",
    "Pizza": "🍕",
    "Paneer Wrap": "🌯",
    "Chicken Biryani": "🍗",
    "French Fries": "🍟",
}


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

with st.sidebar:

    st.title("🍔 Smart Food Corner")

    st.caption(
        "Food Ordering & Restaurant Analytics"
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🍽️ Menu",
            "🛒 Order Food",
            "📦 My Order",
            "🛵 Delivery",
            "📊 Analytics",
        ],
    )

    st.divider()

    st.subheader("Technology")

    st.write("🐍 Python")
    st.write("🧩 Object-Oriented Programming")
    st.write("🎨 Streamlit")

    st.divider()

    st.caption(
        "Portfolio Project • Smart Food Corner"
    )


# ============================================================
# COMMON DATA
# ============================================================

menu_items = restaurant.get_menu()

if st.session_state.customer:
    customer = st.session_state.customer
    orders = customer.order_history
else:
    customer = None
    orders = []


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
        """
        <div class="hero">
            <h1>🍔 Smart Food Corner</h1>
            <p>
                Smart Food Ordering & Restaurant Analytics
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write(
        "A Python OOP-based food ordering application "
        "with customer management, order tracking, "
        "delivery operations and restaurant analytics."
    )

    st.divider()

    st.subheader("📊 Application Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if customer:
            customer_value = customer._name
        else:
            customer_value = "Not Created"

        st.metric(
            "👤 Customer",
            customer_value
        )

    with col2:

        wallet = (
            customer._wallet_balance
            if customer
            else 0
        )

        st.metric(
            "💰 Wallet",
            f"₹{wallet:.0f}"
        )

    with col3:

        if st.session_state.order:
            order_status = (
                st.session_state.order._status
            )
        else:
            order_status = "No Order"

        st.metric(
            "📦 Order",
            order_status
        )

    with col4:

        if st.session_state.delivery_partner:

            partner_status = (
                "Available"
                if st.session_state.delivery_partner.is_available
                else "Busy"
            )

        else:
            partner_status = "Not Created"

        st.metric(
            "🛵 Partner",
            partner_status
        )

    st.divider()

    st.subheader("✨ Explore Smart Food Corner")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            ### 👤 Customer

            Create a customer profile and
            manage wallet balance.
            """
        )

    with col2:

        st.markdown(
            """
            ### 🍽️ Food Ordering

            Browse the menu, select food
            and place an order.
            """
        )

    with col3:

        st.markdown(
            """
            ### 📊 Analytics

            Understand orders, revenue,
            popular food and preferences.
            """
        )

    st.divider()

    st.subheader("🍽️ Restaurant Snapshot")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Restaurant",
            restaurant.name
        )

    with col2:
        st.metric(
            "Location",
            restaurant.location
        )

    with col3:
        st.metric(
            "Menu Items",
            len(menu_items)
        )


# ============================================================
# MENU
# ============================================================

elif page == "🍽️ Menu":

    st.markdown(
        '<div class="section-title">🍽️ Our Menu</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        f"{restaurant.name} • 📍 {restaurant.location}"
    )

    st.write(
        "Explore our available food items."
    )

    st.divider()

    for i in range(0, len(menu_items), 3):

        cols = st.columns(3)

        for j, col in enumerate(cols):

            index = i + j

            if index >= len(menu_items):
                break

            item = menu_items[index]

            with col:

                icon = food_icons.get(
                    item.name,
                    "🍽️"
                )

                st.markdown(
                    f"""
                    <div class="food-card">
                        <div class="food-title">
                            {icon} {item.name}
                        </div>
                        <br>
                        <div class="food-price">
                            ₹{item.price:.0f}
                        </div>
                        <br>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if item.is_veg:
                    st.success("🟢 Vegetarian")
                else:
                    st.error("🔴 Non-Vegetarian")

    st.divider()

    st.subheader("📋 Menu Overview")

    col1, col2, col3 = st.columns(3)

    veg_count = sum(
        1 for item in menu_items
        if item.is_veg
    )

    nonveg_count = sum(
        1 for item in menu_items
        if not item.is_veg
    )

    with col1:
        st.metric(
            "🍽️ Total Items",
            len(menu_items)
        )

    with col2:
        st.metric(
            "🟢 Vegetarian",
            veg_count
        )

    with col3:
        st.metric(
            "🔴 Non-Vegetarian",
            nonveg_count
        )


# ============================================================
# ORDER FOOD
# ============================================================

elif page == "🛒 Order Food":

    st.markdown(
        '<div class="section-title">🛒 Smart Food Ordering</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Select your favourite items and place your order."
    )

    st.divider()

    # --------------------------------------------------------
    # CUSTOMER
    # --------------------------------------------------------

    st.subheader("👤 Customer")

    if customer is None:

        st.info(
            "Create a customer profile before placing an order."
        )

        with st.form("customer_form"):

            name = st.text_input(
                "Full Name",
                placeholder="Enter customer name"
            )

            phone = st.text_input(
                "Phone Number",
                placeholder="Enter phone number"
            )

            address = st.text_input(
                "Delivery Address",
                placeholder="Enter delivery address"
            )

            submit = st.form_submit_button(
                "Create Customer",
                type="primary"
            )

            if submit:

                if name and phone and address:

                    st.session_state.customer = Customer(
                        name,
                        phone,
                        address
                    )

                    st.success(
                        f"Welcome, {name}! 🎉"
                    )

                    st.rerun()

                else:

                    st.warning(
                        "Please fill in all fields."
                    )

    else:

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                f"👤 **{customer._name}**"
            )

        with col2:

            st.info(
                f"💰 Wallet: "
                f"**₹{customer._wallet_balance:.2f}**"
            )

    st.divider()

    # --------------------------------------------------------
    # WALLET
    # --------------------------------------------------------

    st.subheader("💰 Wallet")

    if customer:

        col1, col2 = st.columns([1, 2])

        with col1:

            amount = st.number_input(
                "Amount to Add",
                min_value=0.0,
                step=100.0,
                value=100.0,
                key="wallet_amount"
            )

        with col2:

            st.write("")
            st.write("")

            if st.button(
                "➕ Add Money",
                type="secondary"
            ):

                if amount > 0:

                    customer.add_to_wallet(amount)

                    st.success(
                        f"₹{amount:.2f} added successfully!"
                    )

                    st.rerun()

    st.divider()

    # --------------------------------------------------------
    # FOOD SELECTION
    # --------------------------------------------------------

    st.subheader("🍽️ Select Food")

    if customer:

        selected_items = st.multiselect(
            "Choose food items",
            [
                item.name
                for item in menu_items
            ],
            placeholder="Select items..."
        )

        if selected_items:

            selected_objects = [
                item
                for item in menu_items
                if item.name in selected_items
            ]

            subtotal = sum(
                item.price
                for item in selected_objects
            )

            gst = subtotal * 0.05

            packaging = 20

            total = (
                subtotal
                + gst
                + packaging
            )

            st.divider()

            st.subheader("🧾 Bill Preview")

            bill_col1, bill_col2 = st.columns(2)

            with bill_col1:

                for item in selected_objects:

                    icon = food_icons.get(
                        item.name,
                        "🍽️"
                    )

                    st.write(
                        f"{icon} {item.name} — "
                        f"₹{item.price:.2f}"
                    )

            with bill_col2:

                st.write(
                    f"Subtotal: ₹{subtotal:.2f}"
                )

                st.write(
                    f"GST (5%): ₹{gst:.2f}"
                )

                st.write(
                    f"Packaging: ₹{packaging:.2f}"
                )

                st.markdown(
                    f"### Total: ₹{total:.2f}"
                )

            st.divider()

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
                        "placed successfully!"
                    )

                    st.info(
                        f"🔐 Demo OTP: **{order._otp}**"
                    )

                    st.rerun()

                except Exception as e:

                    st.error(
                        f"Unable to place order: {e}"
                    )

        else:

            st.info(
                "Select food items to see your bill."
            )


# ============================================================
# MY ORDER
# ============================================================

elif page == "📦 My Order":

    st.markdown(
        '<div class="section-title">📦 My Order</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Track your current food order."
    )

    st.divider()

    if st.session_state.order:

        order = st.session_state.order

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Order ID",
                order._order_id
            )

        with col2:

            st.metric(
                "Status",
                order._status
            )

        with col3:

            st.metric(
                "Total Bill",
                f"₹{order.calculate_bill():.2f}"
            )

        st.divider()

        st.subheader("⏱️ Delivery Information")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Estimated Time",
                f"{order.estimated_time()} min"
            )

        with col2:

            if order._status == "Delivered":

                st.success(
                    "🎉 Order delivered successfully!"
                )

            elif order._status == "Accepted":

                st.info(
                    "🛵 Your order is out for delivery."
                )

            else:

                st.warning(
                    "⏳ Waiting for delivery partner."
                )

        st.divider()

        st.subheader("🍽️ Ordered Items")

        for item in order._items:

            icon = food_icons.get(
                item.name,
                "🍽️"
            )

            st.write(
                f"{icon} **{item.name}** — "
                f"₹{item.price:.2f}"
            )

    else:

        st.info(
            "🛒 No order has been placed yet."
        )


# ============================================================
# DELIVERY
# ============================================================

elif page == "🛵 Delivery":

    st.markdown(
        '<div class="section-title">🛵 Delivery Operations</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Manage delivery partners and complete deliveries."
    )

    st.divider()

    # --------------------------------------------------------
    # CREATE PARTNER
    # --------------------------------------------------------

    st.subheader("👤 Delivery Partner")

    with st.form("delivery_partner_form"):

        col1, col2, col3 = st.columns(3)

        with col1:

            partner_name = st.text_input(
                "Partner Name",
                placeholder="Enter partner name"
            )

        with col2:

            partner_phone = st.text_input(
                "Phone Number",
                placeholder="Enter phone number"
            )

        with col3:

            vehicle = st.selectbox(
                "Vehicle",
                [
                    "Bike",
                    "Scooter",
                    "Car"
                ]
            )

        create_partner = st.form_submit_button(
            "Create Delivery Partner",
            type="primary"
        )

        if create_partner:

            if partner_name and partner_phone:

                st.session_state.delivery_partner = (
                    DeliveryPartner(
                        partner_name,
                        partner_phone,
                        vehicle
                    )
                )

                st.success(
                    f"🎉 {partner_name} created successfully!"
                )

                st.rerun()

            else:

                st.warning(
                    "Enter partner name and phone."
                )

    st.divider()

    # --------------------------------------------------------
    # PARTNER STATUS
    # --------------------------------------------------------

    if st.session_state.delivery_partner:

        partner = st.session_state.delivery_partner

        st.subheader("📊 Partner Status")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "👤 Partner",
                partner._name
            )

        with col2:

            status = (
                "Available"
                if partner.is_available
                else "Busy"
            )

            st.metric(
                "Availability",
                status
            )

        with col3:

            st.metric(
                "🛵 Vehicle",
                partner.vehicle
            )

    else:

        st.info(
            "No delivery partner created yet."
        )

    st.divider()

    # --------------------------------------------------------
    # ACCEPT ORDER
    # --------------------------------------------------------

    st.subheader("📦 Accept Order")

    if st.session_state.order is None:

        st.info(
            "Place an order before assigning a delivery partner."
        )

    elif st.session_state.deliver :
