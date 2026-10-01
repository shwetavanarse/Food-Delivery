import streamlit as st
from food_delivery import Customer, DeliveryPartner, MenuItem, Restaurant


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Foodie | Food Delivery",
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

    /* =========================
       GLOBAL
    ========================= */

    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
    );

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #f7f7f8;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* =========================
       HERO
    ========================= */

    .hero {
        background:
            linear-gradient(
                135deg,
                #171717 0%,
                #242424 55%,
                #3b2015 100%
            );

        border-radius: 28px;
        padding: 45px 50px;
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
        box-shadow:
            0 20px 50px rgba(0, 0, 0, 0.12);
    }

    .hero::after {
        content: "🍔";
        position: absolute;
        right: 55px;
        top: 8px;
        font-size: 150px;
        opacity: 0.12;
        transform: rotate(-12deg);
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255, 107, 53, 0.16);
        color: #ff9a76;
        border: 1px solid rgba(255, 107, 53, 0.30);
        padding: 7px 14px;
        border-radius: 30px;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.7px;
        margin-bottom: 15px;
    }

    .hero-title {
        color: white;
        font-size: 44px;
        font-weight: 800;
        line-height: 1.08;
        margin: 0;
    }

    .hero-title span {
        color: #ff7040;
    }

    .hero-subtitle {
        color: #c8c8c8;
        font-size: 15px;
        line-height: 1.6;
        margin-top: 13px;
        max-width: 620px;
    }


    /* =========================
       SECTION HEADINGS
    ========================= */

    .section-title {
        font-size: 25px;
        font-weight: 800;
        color: #191919;
        margin-top: 5px;
        margin-bottom: 4px;
    }

    .section-subtitle {
        color: #777;
        font-size: 13px;
        margin-bottom: 20px;
    }


    /* =========================
       STAT CARDS
    ========================= */

    .stat-card {
        background: white;
        border: 1px solid #ededed;
        border-radius: 18px;
        padding: 20px;
        min-height: 105px;
        box-shadow:
            0 7px 25px rgba(0, 0, 0, 0.04);
    }

    .stat-label {
        color: #888;
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.7px;
    }

    .stat-value {
        color: #202020;
        font-size: 20px;
        font-weight: 800;
        margin-top: 7px;
    }


    /* =========================
       FOOD CARDS
    ========================= */

    .food-card {
        background: white;
        border: 1px solid #ededed;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 14px;
        box-shadow:
            0 7px 24px rgba(0, 0, 0, 0.04);
        min-height: 145px;
    }

    .food-icon {
        width: 58px;
        height: 58px;
        border-radius: 17px;
        background: #fff1eb;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 29px;
        margin-bottom: 13px;
    }

    .food-name {
        font-size: 16px;
        font-weight: 800;
        color: #202020;
    }

    .food-price {
        color: #ff6b35;
        font-size: 16px;
        font-weight: 800;
        margin-top: 4px;
    }

    .veg {
        display: inline-block;
        margin-top: 7px;
        background: #e9f8ef;
        color: #168449;
        border-radius: 7px;
        padding: 3px 8px;
        font-size: 9px;
        font-weight: 800;
    }

    .nonveg {
        display: inline-block;
        margin-top: 7px;
        background: #fff0f0;
        color: #d83c3c;
        border-radius: 7px;
        padding: 3px 8px;
        font-size: 9px;
        font-weight: 800;
    }


    /* =========================
       WHITE CARDS
    ========================= */

    .card {
        background: white;
        border: 1px solid #ededed;
        border-radius: 20px;
        padding: 24px;
        box-shadow:
            0 7px 25px rgba(0, 0, 0, 0.04);
    }

    .card-title {
        font-size: 17px;
        font-weight: 800;
        color: #222;
        margin-bottom: 7px;
    }

    .card-text {
        font-size: 13px;
        line-height: 1.6;
        color: #777;
    }


    /* =========================
       BILL CARD
    ========================= */

    .bill-card {
        background: #171717;
        color: white;
        border-radius: 22px;
        padding: 25px;
        box-shadow:
            0 15px 35px rgba(0, 0, 0, 0.12);
    }

    .bill-title {
        font-size: 18px;
        font-weight: 800;
        margin-bottom: 15px;
    }

    .bill-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        color: #c9c9c9;
        font-size: 13px;
    }

    .bill-total {
        border-top: 1px solid #444;
        margin-top: 10px;
        padding-top: 15px;
        display: flex;
        justify-content: space-between;
        font-size: 19px;
        font-weight: 800;
    }

    .bill-total span:last-child {
        color: #ff8b62;
    }


    /* =========================
       STATUS
    ========================= */

    .status-badge {
        display: inline-block;
        background: #fff0e9;
        color: #f05c2b;
        border-radius: 30px;
        padding: 7px 13px;
        font-size: 11px;
        font-weight: 800;
    }


    /* =========================
       OTP
    ========================= */

    .otp-card {
        background: linear-gradient(
            135deg,
            #fff5f0,
            #ffffff
        );
        border: 1px solid #ffd8ca;
        border-radius: 20px;
        padding: 24px;
        text-align: center;
        margin-top: 15px;
    }

    .otp-label {
        color: #777;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }

    .otp-number {
        color: #ff6b35;
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 8px;
        margin-top: 7px;
    }


    /* =========================
       PROGRESS
    ========================= */

    .progress-card {
        background: white;
        border: 1px solid #ededed;
        border-radius: 17px;
        padding: 17px;
        text-align: center;
        box-shadow:
            0 5px 20px rgba(0, 0, 0, 0.035);
    }

    .progress-icon {
        font-size: 23px;
    }

    .progress-label {
        font-size: 11px;
        font-weight: 700;
        margin-top: 6px;
        color: #333;
    }


    /* =========================
       BUTTONS
    ========================= */

    .stButton > button {
        min-height: 44px;
        border-radius: 12px;
        font-weight: 700;
        border: 1px solid #e6e6e6;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow:
            0 7px 18px rgba(0, 0, 0, 0.08);
    }

    .stButton > button[kind="primary"] {
        background:
            linear-gradient(
                135deg,
                #ff6330,
                #ff8054
            );
        color: white;
        border: none;
    }


    /* =========================
       INPUTS
    ========================= */

    .stTextInput input,
    .stNumberInput input {
        border-radius: 12px !important;
    }

    div[data-baseweb="select"] {
        border-radius: 12px !important;
    }


    /* =========================
       SIDEBAR
    ========================= */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #171717,
                #242424
            );
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }


    /* =========================
       FOOTER
    ========================= */

    .footer {
        text-align: center;
        color: #999;
        font-size: 11px;
        padding: 40px 10px 10px;
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

if "restaurant" not in st.session_state:

    r = Restaurant(
        "Food Hub",
        "Sambhajinagar"
    )

    r.add_item(
        MenuItem("Veg Burger", 120, True)
    )

    r.add_item(
        MenuItem("Pizza", 250, True)
    )

    r.add_item(
        MenuItem("French Fries", 100, True)
    )

    r.add_item(
        MenuItem("Cold Drink", 60, True)
    )

    st.session_state.restaurant = r

if "order" not in st.session_state:
    st.session_state.order = None

if "delivery_partner" not in st.session_state:
    st.session_state.delivery_partner = None


restaurant = st.session_state.restaurant


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:18px 0 25px;
        ">

            <div style="font-size:48px;">
                🍔
            </div>

            <div style="
                font-size:25px;
                font-weight:800;
                color:white;
            ">
                Foodie
            </div>

            <div style="
                font-size:11px;
                color:#aaa;
                margin-top:5px;
            ">
                Smart Food Delivery
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### 🍽️ Restaurant")

    st.markdown(
        f"""
        <div style="
            background:#292929;
            border-radius:15px;
            padding:15px;
        ">

            <div style="
                font-weight:800;
                color:white;
            ">
                {restaurant.name}
            </div>

            <div style="
                color:#aaa;
                font-size:11px;
                margin-top:5px;
            ">
                📍 {restaurant.location}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📋 Order Journey")

    st.markdown(
        """
        <div style="
            color:#ccc;
            font-size:12px;
            line-height:2.2;
        ">

        👤 Customer Profile<br>
        💰 Wallet Balance<br>
        🍽️ Restaurant Menu<br>
        🛒 Place Order<br>
        🛵 Delivery Partner<br>
        📦 Accept Order<br>
        🔐 Verify OTP<br>
        🎉 Complete Delivery

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.customer:

        st.markdown("---")
        st.markdown("### 👤 Current Customer")

        customer = st.session_state.customer

        st.markdown(
            f"""
            <div style="
                background:#292929;
                border-radius:15px;
                padding:15px;
            ">

                <div style="
                    font-weight:800;
                    color:white;
                ">
                    {customer._name}
                </div>

                <div style="
                    color:#aaa;
                    font-size:11px;
                    margin-top:5px;
                ">
                    Wallet:
                    ₹{customer._wallet_balance:.2f}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            ✨ SMART FOOD DELIVERY SYSTEM
        </div>

        <div class="hero-title">
            Good food.<br>
            <span>Good mood.</span>
        </div>

        <div class="hero-subtitle">
            A modern food delivery experience built with
            Python Object-Oriented Programming and Streamlit.
            Create your order, assign a delivery partner,
            verify the OTP and complete the delivery.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DASHBOARD STATS
# ============================================================

customer_active = (
    st.session_state.customer is not None
)

order_active = (
    st.session_state.order is not None
)

partner_active = (
    st.session_state.delivery_partner is not None
)


stat1, stat2, stat3, stat4 = st.columns(4)


with stat1:

    st.markdown(
        """
        <div class="stat-card">

            <div class="stat-label">
                Restaurant
            </div>

            <div class="stat-value">
                🍽️ Food Hub
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with stat2:

    st.markdown(
        f"""
        <div class="stat-card">

            <div class="stat-label">
                Menu Items
            </div>

            <div class="stat-value">
                {len(restaurant.get_menu())}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with stat3:

    st.markdown(
        f"""
        <div class="stat-card">

            <div class="stat-label">
                Customer
            </div>

            <div class="stat-value">
                {"Active" if customer_active else "Not Created"}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with stat4:

    if st.session_state.order:

        current_status = (
            st.session_state.order._status
        )

    else:

        current_status = "No Order"

    st.markdown(
        f"""
        <div class="stat-card">

            <div class="stat-label">
                Order Status
            </div>

            <div class="stat-value">
                {current_status}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# CUSTOMER PROFILE
# ============================================================

st.markdown(
    """
    <div class="section-title">
        👤 Create Your Profile
    </div>

    <div class="section-subtitle">
        Enter your details before placing an order.
    </div>
    """,
    unsafe_allow_html=True,
)


with st.form("customer_form"):

    customer_col1, customer_col2, customer_col3 = (
        st.columns(3)
    )

    with customer_col1:

        name = st.text_input(
            "Full Name",
            placeholder="e.g. Shweta Vanarse",
        )

    with customer_col2:

        phone = st.text_input(
            "Phone Number",
            placeholder="Enter phone number",
        )

    with customer_col3:

        address = st.text_input(
            "Delivery Address",
            placeholder="Enter delivery address",
        )

    customer_submit = st.form_submit_button(
        "Create Customer",
        type="primary",
        use_container_width=True,
    )


if customer_submit:

    if name and phone and address:

        st.session_state.customer = Customer(
            name,
            phone,
            address,
        )

        st.success(
            f"Welcome, {name}! Your profile is ready."
        )

    else:

        st.warning(
            "Please fill in all customer details."
        )


if st.session_state.customer:

    customer = st.session_state.customer

    st.markdown(
        f"""
        <div class="card">

            <div class="card-title">
                👋 Welcome, {customer._name}
            </div>

            <div class="card-text">

                📞 {customer._phone}

                <br>

                📍 {customer._address}

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# WALLET
# ============================================================

st.markdown(
    """
    <div class="section-title">
        💰 Wallet
    </div>

    <div class="section-subtitle">
        Add balance to your food delivery wallet.
    </div>
    """,
    unsafe_allow_html=True,
)


wallet_col1, wallet_col2 = st.columns(
    [1.5, 1]
)


with wallet_col1:

    if st.session_state.customer:

        amount = st.number_input(
            "Amount to Add (₹)",
            min_value=0.0,
            step=50.0,
            format="%.2f",
        )

        if st.button(
            "＋ Add Balance",
            use_container_width=True,
        ):

            if amount > 0:

                st.session_state.customer.add_to_wallet(
                    amount
                )

                st.success(
                    f"₹{amount:.2f} added to wallet."
                )

            else:

                st.warning(
                    "Enter an amount greater than ₹0."
                )

    else:

        st.info(
            "Create a customer first to use the wallet."
        )


with wallet_col2:

    if st.session_state.customer:

        balance = (
            st.session_state.customer._wallet_balance
        )

    else:

        balance = 0.0

    st.markdown(
        f"""
        <div class="stat-card">

            <div class="stat-label">
                Available Balance
            </div>

            <div class="stat-value"
                 style="color:#ff6b35;">
                ₹{balance:.2f}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# RESTAURANT MENU
# ============================================================

st.markdown(
    f"""
    <div class="section-title">
        🍽️ {restaurant.name}
    </div>

    <div class="section-subtitle">
        📍 {restaurant.location}
        &nbsp; • &nbsp;
        Fresh food, simple ordering
    </div>
    """,
    unsafe_allow_html=True,
)


food_emojis = {
    "Veg Burger": "🍔",
    "Pizza": "🍕",
    "French Fries": "🍟",
    "Cold Drink": "🥤",
    "Paneer Wrap": "🌯",
    "Chicken Biryani": "🍗",
}


menu = restaurant.get_menu()


for start in range(0, len(menu), 3):

    cols = st.columns(3)

    for index, col in enumerate(cols):

        actual_index = start + index

        if actual_index >= len(menu):
            continue

        item = menu[actual_index]

        emoji = food_emojis.get(
            item.name,
            "🍽️",
        )

        if item.is_veg:

            badge = (
                '<span class="veg">● VEG</span>'
            )

        else:

            badge = (
                '<span class="nonveg">● NON-VEG</span>'
            )

        with col:

            st.markdown(
                f"""
                <div class="food-card">

                    <div class="food-icon">
                        {emoji}
                    </div>

                    <div class="food-name">
                        {item.name}
                    </div>

                    <div class="food-price">
                        ₹{item.price:.2f}
                    </div>

                    {badge}

                </div>
                """,
                unsafe_allow_html=True,
            )


st.divider()


# ============================================================
# PLACE ORDER
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🛒 Build Your Order
    </div>

    <div class="section-subtitle">
        Choose your favorite items and review your bill.
    </div>
    """,
    unsafe_allow_html=True,
)


if st.session_state.customer:

    selected = st.multiselect(
        "Select food items",
        [x.name for x in menu],
        placeholder="Choose one or more items...",
    )

    if selected:

        selected_objects = [
            x
            for x in menu
            if x.name in selected
        ]

        subtotal = sum(
            x.price
            for x in selected_objects
        )

        gst = subtotal * 0.05

        packaging = 20

        total = (
            subtotal
            + gst
            + packaging
        )

        order_col1, order_col2 = st.columns(
            [1.35, 1]
        )


        with order_col1:

            st.markdown(
                "### 🍴 Selected Items"
            )

            for item in selected_objects:

                emoji = food_emojis.get(
                    item.name,
                    "🍽️",
                )

                st.markdown(
                    f"""
                    <div style="
                        background:white;
                        border:1px solid #ededed;
                        border-radius:14px;
                        padding:13px 16px;
                        margin-bottom:8px;
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                    ">

                        <span>
                            {emoji}
                            &nbsp;
                            <b>{item.name}</b>
                        </span>

                        <span style="
                            color:#ff6b35;
                            font-weight:800;
                        ">
                            ₹{item.price:.2f}
                        </span>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )


        with order_col2:

            st.markdown(
                f"""
                <div class="bill-card">

                    <div class="bill-title">
                        💳 Bill Summary
                    </div>

                    <div class="bill-row">
                        <span>Subtotal</span>
                        <span>₹{subtotal:.2f}</span>
                    </div>

                    <div class="bill-row">
                        <span>GST · 5%</span>
                        <span>₹{gst:.2f}</span>
                    </div>

                    <div class="bill-row">
                        <span>Packaging</span>
                        <span>₹{packaging:.2f}</span>
                    </div>

                    <div class="bill-total">
                        <span>Total</span>
                        <span>₹{total:.2f}</span>
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


        st.markdown("<br>", unsafe_allow_html=True)


        if st.button(
            "🛍️ Place Order",
            type="primary",
            use_container_width=True,
        ):

            items = [
                x
                for x in menu
                if x.name in selected
            ]

            st.session_state.order = (
                st.session_state.customer.place_order(
                    restaurant,
                    items,
                )
            )

            order = st.session_state.order

            st.success(
                f"🎉 Order #{order._order_id} placed successfully!"
            )

            st.markdown(
                f"""
                <div class="otp-card">

                    <div class="otp-label">
                        🔐 DELIVERY OTP
                    </div>

                    <div class="otp-number">
                        1234
                    </div>

                    <div style="
                        color:#888;
                        font-size:10px;
                        margin-top:8px;
                    ">
                        Demo OTP for this project
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

    else:

        st.info(
            "Select at least one food item to build your order."
        )

else:

    st.warning(
        "Create a customer before placing an order."
    )


st.divider()


# ============================================================
# ORDER TRACKING
# ============================================================

st.markdown(
    """
    <div class="section-title">
        📦 Order Tracking
    </div>

    <div class="section-subtitle">
        Follow your order from restaurant to doorstep.
    </div>
    """,
    unsafe_allow_html=True,
)


if st.session_state.order:

    order = st.session_state.order

    status = order._status


    track1, track2, track3 = st.columns(3)


    with track1:

        st.markdown(
            f"""
            <div class="stat-card">

                <div class="stat-label">
                    Order ID
                </div>

                <div class="stat-value">
                    #{order._order_id}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    with track2:

        st.markdown(
            f"""
            <div class="stat-card">

                <div class="stat-label">
                    Current Status
                </div>

                <div style="
                    margin-top:9px;
                ">

                    <span class="status-badge">
                        {status}
                    </span>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    with track3:

        st.markdown(
            f"""
            <div class="stat-card">

                <div class="stat-label">
                    Estimated Time
                </div>

                <div class="stat-value">
                    ⏱️ {order.estimated_time()} min
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # Progress stages

    if status == "Order Accepted":

        current_stage = 1

    elif status == "Delivered":

        current_stage = 2

    else:

        current_stage = 0


    stage_names = [
        ("🛒", "Order Placed"),
        ("🛵", "Order Accepted"),
        ("🎉", "Delivered"),
    ]


    progress_cols = st.columns(3)


    for i, (icon, label) in enumerate(stage_names):

        with progress_cols[i]:

            if i <= current_stage:

                progress_icon = "🟢"

            else:

                progress_icon = "⚪"

            st.markdown(
                f"""
                <div class="progress-card">

                    <div class="progress-icon">
                        {progress_icon}
                    </div>

                    <div class="progress-label">
                        {icon} {label}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


else:

    st.markdown(
        """
        <div class="card">

            <div style="
                text-align:center;
                padding:15px;
            ">

                <div style="
                    font-size:40px;
                ">
                    📦
                </div>

                <div class="card-title">
                    No active order
                </div>

                <div class="card-text">
                    Your order status will appear here
                    after you place an order.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# DELIVERY PARTNER
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🛵 Delivery Partner
    </div>

    <div class="section-subtitle">
        Create a delivery partner for your order.
    </div>
    """,
    unsafe_allow_html=True,
)


with st.form("delivery_form"):

    dp_col1, dp_col2, dp_col3 = st.columns(3)

    with dp_col1:

        dp_name = st.text_input(
            "Delivery Partner Name",
            placeholder="Enter partner name",
        )

    with dp_col2:

        dp_phone = st.text_input(
            "Delivery Partner Phone",
            placeholder="Enter phone number",
        )

    with dp_col3:

        vehicle = st.selectbox(
            "Vehicle",
            [
                "Bike",
                "Scooter",
                "Car",
            ],
        )

    delivery_submit = st.form_submit_button(
        "Create Delivery Partner",
        type="primary",
        use_container_width=True,
    )


if delivery_submit:

    if dp_name and dp_phone:

        st.session_state.delivery_partner = (
            DeliveryPartner(
                dp_name,
                dp_phone,
                vehicle,
            )
        )

        st.success(
            f"🛵 {dp_name} is ready for delivery!"
        )

    else:

        st.warning(
            "Please fill in all delivery partner details."
        )


if st.session_state.delivery_partner:

    partner = (
        st.session_state.delivery_partner
    )

    availability = (
        "Available"
        if partner.is_available
        else "Busy"
    )

    st.markdown(
        f"""
        <div class="card">

            <div style="
                display:flex;
                align-items:center;
                gap:18px;
            ">

                <div class="food-icon">
                    🛵
                </div>

                <div>

                    <div class="card-title">
                        {partner._name}
                    </div>

                    <div class="card-text">
                        📞 {partner._phone}
                        <br>
                        🛵 {partner.vehicle}
                    </div>

                </div>

                <div style="
                    margin-left:auto;
                    text-align:right;
                ">

                    <div class="stat-label">
                        AVAILABILITY
                    </div>

                    <div style="
                        color:#168449;
                        font-weight:800;
                        margin-top:5px;
                    ">
                        {availability}
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# ACCEPT ORDER
# ============================================================

st.markdown(
    """
    <div class="section-title">
        📦 Accept Order
    </div>

    <div class="section-subtitle">
        Let the delivery partner accept the customer's order.
    </div>
    """,
    unsafe_allow_html=True,
)


if st.session_state.order and st.session_state.delivery_partner:

    if st.button(
        "✅ Accept Order",
        type="primary",
        use_container_width=True,
    ):

        st.session_state.delivery_partner.accept_order(
            st.session_state.order
        )

        st.success(
            "🛵 Order accepted by delivery partner!"
        )

else:

    st.info(
        "Create both an order and delivery partner first."
    )


st.divider()


# ============================================================
# OTP VERIFICATION
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🔐 Verify Delivery OTP
    </div>

    <div class="section-subtitle">
        Verify the customer's OTP before completing delivery.
    </div>
    """,
    unsafe_allow_html=True,
)


if st.session_state.order:

    st.markdown(
        """
        <div class="otp-card">

            <div class="otp-label">
                DEMO OTP
            </div>

            <div class="otp-number">
                1234
            </div>

            <div style="
                color:#888;
                font-size:10px;
                margin-top:5px;
            ">
                This is displayed only for project demonstration.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    otp = st.number_input(
        "Enter OTP",
        min_value=0,
        max_value=9999,
        step=1,
        key="verification_otp",
    )


    if st.button(
        "🔐 Verify OTP",
        use_container_width=True,
    ):

        if st.session_state.order.verify_otp(
            otp
        ):

            st.success(
                "✅ OTP is correct!"
            )

        else:

            st.error(
                "❌ Incorrect OTP."
            )

else:

    st.info(
        "Place an order first to verify OTP."
    )


st.divider()


# ============================================================
# COMPLETE DELIVERY
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🎉 Complete Delivery
    </div>

    <div class="section-subtitle">
        Enter the OTP and complete the delivery.
    </div>
    """,
    unsafe_allow_html=True,
)


if (
    st.session_state.order
    and st.session_state.delivery_partner
):

    delivery_otp = st.number_input(
        "OTP to complete delivery",
        min_value=0,
        max_value=9999,
        step=1,
        key="delivery_otp",
    )


    if st.button(
        "🎉 Complete Delivery",
        type="primary",
        use_container_width=True,
    ):

        success = (
            st.session_state.delivery_partner.deliver(
                st.session_state.order,
                delivery_otp,
            )
        )


        if success:

            st.balloons()

            st.success(
                "🎉 Delivery completed successfully!"
            )

        else:

            st.error(
                "❌ Delivery failed. Please check the OTP."
            )

else:

    st.info(
        "Create an order and delivery partner first."
    )


st.divider()


# ============================================================
# FINAL RECEIPT
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🧾 Final Order Summary
    </div>

    <div class="section-subtitle">
        Your complete order information.
    </div>
    """,
    unsafe_allow_html=True,
)


if st.session_state.order:

    order = st.session_state.order


    receipt_col1, receipt_col2 = st.columns(
        [1.3, 1]
    )


    with receipt_col1:

        customer_name_display = (
            st.session_state.customer._name
            if st.session_state.customer
            else "Guest"
        )


        st.markdown(
            f"""
            <div class="card">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                    margin-bottom:20px;
                ">

                    <div>

                        <div class="card-title">
                            🍔 Food Hub
                        </div>

                        <div class="card-text">
                            📍 {restaurant.location}
                        </div>

                    </div>

                    <span class="status-badge">
                        {order._status}
                    </span>

                </div>


                <div style="
                    border-top:1px solid #eee;
                    padding-top:15px;
                ">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-bottom:12px;
                    ">

                        <span style="color:#777;">
                            Order ID
                        </span>

                        <b>
                            #{order._order_id}
                        </b>

                    </div>


                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-bottom:12px;
                    ">

                        <span style="color:#777;">
                            Customer
                        </span>

                        <b>
                            {customer_name_display}
                        </b>

                    </div>


                    <div style="
                        display:flex;
                        justify-content:space-between;
                    ">

                        <span style="color:#777;">
                            Total Bill
                        </span>

                        <b style="
                            color:#ff6b35;
                            font-size:18px;
                        ">
                            ₹{order.calculate_bill():.2f}
                        </b>

                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    with receipt_col2:

        if st.session_state.delivery_partner:

            partner = (
                st.session_state.delivery_partner
            )

            partner_name_display = partner._name
            vehicle_display = partner.vehicle

        else:

            partner_name_display = "Not assigned"
            vehicle_display = "-"


        st.markdown(
            f"""
            <div class="card">

                <div class="food-icon">
                    🛵
                </div>

                <div class="card-title">
                    Delivery Details
                </div>

                <div class="card-text">

                    <b>Delivery Partner</b>
                    <br>
                    {partner_name_display}

                    <br><br>

                    <b>Vehicle</b>
                    <br>
                    {vehicle_display}

                    <br><br>

                    <b>Restaurant</b>
                    <br>
                    {restaurant.name}

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


else:

    st.markdown(
        """
        <div class="card">

            <div style="
                text-align:center;
                padding:25px;
            ">

                <div style="
                    font-size:45px;
                ">
                    🧾
                </div>

                <div class="card-title">
                    No receipt yet
                </div>

                <div class="card-text">
                    Your final order receipt will appear
                    here after placing an order.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        🍔 <b>Foodie</b> · OOP Food Delivery System

        <br><br>

        Built with Python · Object-Oriented Programming · Streamlit

        <br>

        © 2026 Foodie · Portfolio Project

    </div>
    """,
    unsafe_allow_html=True,
)
