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

    /* ================================
       MAIN APP
       ================================ */

    .main {
        background-color: #f7f8fa;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }


    /* ================================
       SIDEBAR
       ================================ */

    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #eeeeee;
    }

    [data-testid="stSidebar"] h1 {
        font-size: 24px;
        font-weight: 800;
    }

    [data-testid="stSidebar"] .stRadio label {
        font-weight: 500;
    }

 /* ================================
   METRIC CARDS
   ================================ */

[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 16px 18px;
    border-radius: 18px;
    border: 1px solid #eeeeee;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
    min-height: 105px;
}

[data-testid="stMetricLabel"] {
    font-size: 14px;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    font-size: 25px;
    font-weight: 750;
    white-space: normal;
    overflow: visible;
    text-overflow: clip;
    line-height: 1.2;
}

/* ================================
   FEATURE CARDS
   ================================ */

.feature-card {
    background-color: #ffffff;
    border: 1px solid #eeeeee;
    border-radius: 20px;
    padding: 24px;
    min-height: 170px;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.04);
    transition: all 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
}

.feature-icon {
    font-size: 30px;
    margin-bottom: 10px;
}

.feature-title {
    font-size: 20px;
    font-weight: 750;
    margin-bottom: 8px;
}

.feature-text {
    font-size: 14px;
    line-height: 1.6;
    color: #666666;
}
    /* ================================
       HERO SECTION
       ================================ */

    .hero {
        padding: 38px 40px;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            #ff6b35 0%,
            #ff8c42 100%
        );
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 10px 30px rgba(255, 107, 53, 0.20);
    }

    .hero h1 {
        font-size: 44px;
        font-weight: 800;
        margin: 0 0 8px 0;
        letter-spacing: -1px;
    }

    .hero p {
        font-size: 17px;
        margin: 0;
        opacity: 0.95;
    }


    /* ================================
       SECTION TITLES
       ================================ */

    .section-title {
        font-size: 30px;
        font-weight: 800;
        margin-bottom: 5px;
        letter-spacing: -0.5px;
    }

    .small-text {
        color: #666666;
    }


    /* ================================
       FOOD CARDS
       ================================ */

    .food-card {
        padding: 24px;
        min-height: 135px;
        border-radius: 20px;
        background: #ffffff;
        border: 1px solid #eeeeee;
        margin-bottom: 12px;
        box-shadow: 0 5px 18px rgba(0, 0, 0, 0.05);
        transition: all 0.2s ease;
    }

    .food-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
    }

    .food-title {
        font-size: 21px;
        font-weight: 750;
        color: #222222;
    }

    .food-price {
        font-size: 22px;
        font-weight: 800;
        color: #ff6b35;
    }

/* ================================
   PREMIUM KPI CARDS
   ================================ */

.kpi-card {
    background: #ffffff;
    border: 1px solid #eeeeee;
    border-radius: 18px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.05);
    transition: all 0.25s ease;
}

.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.09);
}

.kpi-label {
    font-size: 14px;
    color: #777777;
    font-weight: 600;
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 25px;
    font-weight: 800;
    color: #343744;
}

.kpi-icon {
    font-size: 24px;
    margin-bottom: 8px;
}

    /* ================================
       METRIC CARDS
       ================================ */

    [data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 18px;
        border-radius: 18px;
        border: 1px solid #eeeeee;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
    }


    /* ================================
       BUTTONS
       ================================ */

    .stButton > button {
        border-radius: 10px;
        font-weight: 650;
        min-height: 42px;
    }


    /* ================================
       INPUT FIELDS
       ================================ */

    .stTextInput input,
    .stNumberInput input {
        border-radius: 10px;
    }

    .stSelectbox div[data-baseweb="select"] {
        border-radius: 10px;
    }


    /* ================================
       STATUS / INFO BOXES
       ================================ */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ================================
       DIVIDERS
       ================================ */

    hr {
        margin-top: 25px;
        margin-bottom: 25px;
        border: none;
        border-top: 1px solid #e8e8e8;
    }


    /* ================================
       FOOTER
       ================================ */

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

    col1, col2, col3, col4 = st.columns(4, gap="medium")

    # Customer
    with col1:

        customer_value = (
            customer._name
            if customer
            else "Not Created"
        )

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon">👤</div>
                <div class="kpi-label">CUSTOMER</div>
                <div class="kpi-value">{customer_value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Wallet
    with col2:

        wallet = (
            customer._wallet_balance
            if customer
            else 0
        )

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon">💰</div>
                <div class="kpi-label">WALLET BALANCE</div>
                <div class="kpi-value">₹{wallet:.0f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Order
    with col3:

        order_status = (
            st.session_state.order._status
            if st.session_state.order
            else "No Order"
        )

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon">📦</div>
                <div class="kpi-label">ORDER STATUS</div>
                <div class="kpi-value">{order_status}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Delivery Partner
    with col4:

        if st.session_state.delivery_partner:

            partner_status = (
                "Available"
                if st.session_state.delivery_partner.is_available
                else "Busy"
            )

        else:

            partner_status = "Not Created"

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-icon">🛵</div>
                <div class="kpi-label">DELIVERY PARTNER</div>
                <div class="kpi-value">{partner_status}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.subheader("✨ Explore Smart Food Corner")

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">👤</div>
                <div class="feature-title">Customer</div>
                <div class="feature-text">
                    Create a customer profile,
                    manage your wallet and
                    place food orders.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🍽️</div>
                <div class="feature-title">Food Ordering</div>
                <div class="feature-text">
                    Explore the menu,
                    select your favourite food
                    and place an order.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">Analytics</div>
                <div class="feature-text">
                    Analyze orders, revenue,
                    popular food items and
                    customer preferences.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
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
                    "Please enter partner name and phone number."
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
            "🛒 Place an order before assigning a delivery partner."
        )

    elif st.session_state.delivery_partner is None:

        st.info(
            "👤 Create a delivery partner first."
        )

    else:

        order = st.session_state.order
        partner = st.session_state.delivery_partner

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"**Order ID:** {order._order_id}"
            )

            st.write(
                f"**Order Status:** {order._status}"
            )

        with col2:

            if order._status == "Placed":

                if partner.is_available:

                    if st.button(
                        "✅ Accept Order",
                        type="primary",
                        use_container_width=True
                    ):

                        partner.accept_order(order)

                        st.success(
                            f"Order {order._order_id} accepted successfully!"
                        )

                        st.rerun()

                else:

                    st.warning(
                        "⚠️ Delivery partner is currently busy."
                    )

            elif order._status == "Accepted":

                st.info(
                    "🛵 This order has already been accepted."
                )

            elif order._status == "Delivered":

                st.success(
                    "🎉 This order has already been delivered."
                )

    st.divider()
    # --------------------------------------------------------
    # COMPLETE DELIVERY
    # --------------------------------------------------------

    st.subheader("🚚 Complete Delivery")

    if st.session_state.order is None:

        st.info(
            "No order available."
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
                "⚠️ Accept the order before completing delivery."
            )

        elif order._status == "Accepted":

            st.info(
                "📍 Order is out for delivery."
            )

            if st.button(
                "🎉 Mark as Delivered",
                type="primary",
                use_container_width=True
            ):

                try:

                    # Use the demo OTP internally.
                    # User does not need to enter it.
                    partner.deliver(
                        order,
                        order._otp
                    )

                    if order._status == "Delivered":

                        st.success(
                            f"🎉 Order {order._order_id} "
                            "delivered successfully!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Unable to complete delivery."
                        )

                except Exception as e:

                    st.error(
                        f"Unable to complete delivery: {e}"
                    )

        elif order._status == "Delivered":

            st.success(
                "🎉 This order has already been delivered."
            )
# ============================================================
# ANALYTICS
# ============================================================

elif page == "📊 Analytics":

    st.markdown(
        '<div class="section-title">📊 Restaurant Analytics</div>',
        unsafe_allow_html=True,
    )

    st.caption(
        "Understand orders, revenue and customer preferences."
    )

    st.divider()

    if customer:

        orders = customer.order_history

    else:

        orders = []

    # --------------------------------------------------------
    # KPIs
    # --------------------------------------------------------

    total_orders = len(orders)

    total_revenue = sum(
        order.calculate_bill()
        for order in orders
    )

    average_order_value = (
        total_revenue / total_orders
        if total_orders
        else 0
    )

    delivered_orders = sum(
        1
        for order in orders
        if order._status == "Delivered"
    )

    placed_orders = sum(
        1
        for order in orders
        if order._status == "Placed"
    )

    accepted_orders = sum(
        1
        for order in orders
        if order._status == "Accepted"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "📦 Total Orders",
            total_orders
        )

    with col2:

        st.metric(
            "💰 Revenue",
            f"₹{total_revenue:.2f}"
        )

    with col3:

        st.metric(
            "📈 Avg Order Value",
            f"₹{average_order_value:.2f}"
        )

    with col4:

        st.metric(
            "🎉 Delivered",
            delivered_orders
        )

    st.divider()

    # --------------------------------------------------------
    # ORDER STATUS
    # --------------------------------------------------------

    st.subheader("📦 Order Status")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🟡 Placed",
            placed_orders
        )

    with col2:

        st.metric(
            "🔵 Accepted",
            accepted_orders
        )

    with col3:

        st.metric(
            "🟢 Delivered",
            delivered_orders
        )

    if not orders:

        st.divider()

        st.info(
            "Place orders to generate restaurant analytics."
        )

    else:

        # ----------------------------------------------------
        # ITEM COUNTS
        # ----------------------------------------------------

        item_counts = {}

        for order in orders:

            for item in order._items:

                item_counts[item.name] = (
                    item_counts.get(item.name, 0) + 1
                )

        sorted_items = sorted(
            item_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        st.divider()

        st.subheader("🍽️ Popular Food Items")

        for rank, (name, count) in enumerate(
            sorted_items,
            start=1
        ):

            st.write(
                f"**#{rank} {name}** — "
                f"{count} order(s)"
            )

        st.divider()

        # ----------------------------------------------------
        # FOOD PREFERENCE
        # ----------------------------------------------------

        st.subheader("🥗 Food Preference")

        veg_orders = 0
        nonveg_orders = 0

        for order in orders:

            for item in order._items:

                if item.is_veg:
                    veg_orders += 1
                else:
                    nonveg_orders += 1

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🟢 Vegetarian",
                veg_orders
            )

        with col2:

            st.metric(
                "🔴 Non-Vegetarian",
                nonveg_orders
            )

        st.divider()

        # ----------------------------------------------------
        # CHARTS
        # ----------------------------------------------------

        st.subheader("📈 Performance Dashboard")

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:

            st.write("Order Status")

            status_data = {
                "Placed": placed_orders,
                "Accepted": accepted_orders,
                "Delivered": delivered_orders,
            }

            st.bar_chart(status_data)

        with chart_col2:

            st.write("Popular Food")

            popular_data = {
                item_name: count
                for item_name, count
                in sorted_items
            }

            st.bar_chart(popular_data)

        st.divider()

        # ----------------------------------------------------
        # BUSINESS INSIGHTS
        # ----------------------------------------------------

        st.subheader("💡 Business Insights")

        top_item = sorted_items[0][0]
        top_item_count = sorted_items[0][1]

        st.success(
            f"🏆 Most ordered item: **{top_item}** "
            f"with {top_item_count} order(s)."
        )

        st.info(
            f"💰 Total restaurant revenue: "
            f"**₹{total_revenue:.2f}**"
        )

        st.info(
            f"📈 Average order value: "
            f"**₹{average_order_value:.2f}**"
        )

        if veg_orders > nonveg_orders:

            st.success(
                "🥗 Vegetarian food is currently "
                "more popular."
            )

        elif nonveg_orders > veg_orders:

            st.warning(
                "🍗 Non-vegetarian food is currently "
                "more popular."
            )

        else:

            st.info(
                "⚖️ Both food categories have "
                "equal order counts."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🍔 Smart Food Corner • "
    "Python OOP + Streamlit • "
    "Portfolio Project"
)
