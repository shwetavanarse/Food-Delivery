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
# PREMIUM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------------- GLOBAL ---------------- */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    * {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 0%, rgba(255, 107, 53, 0.08), transparent 25%),
            radial-gradient(circle at 90% 10%, rgba(255, 193, 7, 0.07), transparent 25%),
            #fafafa;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    /* Hide Streamlit branding */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* ---------------- SIDEBAR ---------------- */

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #171717 0%, #242424 100%);
        border-right: 1px solid #333;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* ---------------- HERO ---------------- */

    .hero {
        background: linear-gradient(
            135deg,
            #171717 0%,
            #252525 55%,
            #3a2118 100%
        );
        border-radius: 28px;
        padding: 42px 48px;
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 50px rgba(0,0,0,0.12);
    }

    .hero::after {
        content: "🍔";
        position: absolute;
        right: 50px;
        top: 15px;
        font-size: 130px;
        opacity: 0.13;
        transform: rotate(-10deg);
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255, 107, 53, 0.18);
        color: #ff8b62;
        border: 1px solid rgba(255, 107, 53, 0.3);
        padding: 7px 14px;
        border-radius: 30px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 14px;
    }

    .hero-title {
        color: white;
        font-size: 42px;
        font-weight: 800;
        line-height: 1.1;
        margin: 0;
    }

    .hero-title span {
        color: #ff6b35;
    }

    .hero-subtitle {
        color: #cfcfcf;
        font-size: 16px;
        margin-top: 12px;
        max-width: 600px;
    }

    /* ---------------- SECTION HEADINGS ---------------- */

    .section-title {
        font-size: 25px;
        font-weight: 800;
        color: #171717;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .section-subtitle {
        color: #777;
        font-size: 14px;
        margin-bottom: 20px;
    }

    /* ---------------- CARDS ---------------- */

    .premium-card {
        background: white;
        border: 1px solid #eeeeee;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.045);
        transition: 0.2s ease;
        height: 100%;
    }

    .premium-card:hover {
        box-shadow: 0 12px 35px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }

    .card-icon {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        background: #fff1eb;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 23px;
        margin-bottom: 14px;
    }

    .card-title {
        font-size: 17px;
        font-weight: 750;
        color: #222;
        margin-bottom: 6px;
    }

    .card-text {
        color: #777;
        font-size: 13px;
        line-height: 1.5;
    }

    /* ---------------- MENU CARDS ---------------- */

    .food-card {
        background: white;
        border: 1px solid #eeeeee;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 12px;
        box-shadow: 0 6px 22px rgba(0,0,0,0.04);
    }

    .food-emoji {
        background: #fff3ed;
        border-radius: 16px;
        width: 58px;
        height: 58px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
    }

    .food-name {
        font-size: 16px;
        font-weight: 750;
        color: #222;
    }

    .food-price {
        color: #ff6b35;
        font-weight: 800;
        font-size: 16px;
    }

    .veg-badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 8px;
        background: #eaf8ef;
        color: #198754;
        font-size: 10px;
        font-weight: 700;
        margin-top: 5px;
    }

    .nonveg-badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 8px;
        background: #fff0f0;
        color: #dc3545;
        font-size: 10px;
        font-weight: 700;
        margin-top: 5px;
    }

    /* ---------------- STAT CARDS ---------------- */

    .stat-card {
        background: white;
        border: 1px solid #eeeeee;
        border-radius: 18px;
        padding: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.04);
    }

    .stat-label {
        font-size: 12px;
        color: #888;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stat-value {
        font-size: 25px;
        font-weight: 800;
        color: #202020;
        margin-top: 5px;
    }

    /* ---------------- BILL ---------------- */

    .bill-card {
        background: #171717;
        color: white;
        border-radius: 22px;
        padding: 25px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.12);
    }

    .bill-row {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        color: #cccccc;
        font-size: 14px;
    }

    .bill-total {
        border-top: 1px solid #444;
        margin-top: 10px;
        padding-top: 15px;
        display: flex;
        justify-content: space-between;
        font-size: 20px;
        font-weight: 800;
        color: white;
    }

    .bill-total span:last-child {
        color: #ff8b62;
    }

    /* ---------------- STATUS ---------------- */

    .status-card {
        background: white;
        border-radius: 22px;
        border: 1px solid #eeeeee;
        padding: 25px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.05);
    }

    .status-badge {
        display: inline-block;
        padding: 7px 13px;
        border-radius: 30px;
        background: #fff1eb;
        color: #ff6b35;
        font-weight: 700;
        font-size: 12px;
    }

    /* ---------------- OTP ---------------- */

    .otp-card {
        background: linear-gradient(135deg, #fff5ef, #fff);
        border: 1px solid #ffd8c9;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
    }

    .otp-title {
        font-size: 13px;
        color: #777;
        font-weight: 600;
    }

    .otp-number {
        color: #ff6b35;
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 8px;
        margin-top: 8px;
    }

    /* ---------------- FOOTER ---------------- */

    .footer {
        text-align: center;
        padding: 35px 10px 10px;
        color: #999;
        font-size: 12px;
    }

    /* ---------------- BUTTONS ---------------- */

    .stButton > button {
        border-radius: 12px;
        font-weight: 700;
        min-height: 44px;
        border: 1px solid #eeeeee;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.08);
    }

    /* Primary buttons */

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #ff6b35, #ff8557);
        border: none;
        color: white;
    }

    /* ---------------- INPUTS ---------------- */

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"],
    .stMultiSelect div[data-baseweb="select"] {
        border-radius: 12px !important;
    }

    /* ---------------- DIVIDER ---------------- */

    hr {
        margin-top: 35px;
        margin-bottom: 35px;
        border: none;
        border-top: 1px solid #eeeeee;
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

if "restaurant" not in st.session_state:

    restaurant = Restaurant(
        "Food Corner",
        "Aurangabad"
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


if "order" not in st.session_state:
    st.session_state.order = None


restaurant = st.session_state.restaurant


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:20px 0 25px;
        ">
            <div style="font-size:48px;">🍔</div>
            <div style="
                font-size:24px;
                font-weight:800;
                color:white;
            ">
                Foodie
            </div>
            <div style="
                font-size:12px;
                color:#aaa;
                margin-top:5px;
            ">
                OOP Food Delivery
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### 📍 Restaurant")

    st.markdown(
        f"""
        <div style="
            background:#292929;
            padding:15px;
            border-radius:15px;
            margin-bottom:20px;
        ">
            <div style="font-weight:700;">
                {restaurant.name}
            </div>
            <div style="
                color:#aaa;
                font-size:12px;
                margin-top:5px;
            ">
                📍 {restaurant.location}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📋 Order Flow")

    st.markdown(
        """
        <div style="line-height:2.2; color:#ccc; font-size:13px;">
            👤 Create Customer<br>
            💰 Add Wallet Balance<br>
            🍽️ Choose Food<br>
            🛒 Place Order<br>
            🛵 Assign Delivery Partner<br>
            📦 Accept Order<br>
            🔐 Verify OTP<br>
            🎉 Complete Delivery
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    if st.session_state.customer:

        st.markdown("### 👤 Customer")

        st.markdown(
            f"""
            <div style="
                background:#292929;
                padding:15px;
                border-radius:15px;
            ">
                <div style="font-weight:700;">
                    {st.session_state.customer._name}
                </div>
                <div style="
                    color:#aaa;
                    font-size:12px;
                    margin-top:6px;
                ">
                    Wallet: ₹
                    {st.session_state.customer._wallet_balance:.2f}
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
            ✨ SMART FOOD DELIVERY
        </div>

        <div class="hero-title">
            Delicious food.<br>
            <span>Delivered simply.</span>
        </div>

        <div class="hero-subtitle">
            A modern food delivery experience powered by
            Object-Oriented Programming and Streamlit.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# TOP STATS
# ============================================================

customer_exists = st.session_state.customer is not None
order_exists = st.session_state.order is not None
partner_exists = st.session_state.delivery_partner is not None

stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">Restaurant</div>
            <div class="stat-value">🍽️ Food Corner</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with stat2:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">Menu Items</div>
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
            <div class="stat-label">Customer</div>
            <div class="stat-value">
                {"Active" if customer_exists else "Not Created"}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with stat4:

    if st.session_state.order:
        status_value = st.session_state.order._status
    else:
        status_value = "No Order"

    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">Order Status</div>
            <div class="stat-value">
                {status_value}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# CUSTOMER
# ============================================================

st.markdown(
    """
    <div class="section-title">
        👤 Your Profile
    </div>

    <div class="section-subtitle">
        Create your customer profile before placing an order.
    </div>
    """,
    unsafe_allow_html=True,
)


col1, col2, col3 = st.columns(3)

with col1:
    customer_name = st.text_input(
        "Full Name",
        placeholder="Enter your name",
    )

with col2:
    customer_phone = st.text_input(
        "Phone Number",
        placeholder="Enter phone number",
    )

with col3:
    customer_address = st.text_input(
        "Delivery Address",
        placeholder="Enter delivery address",
    )


if st.button(
    "Create Customer",
    type="primary",
    use_container_width=True,
):

    if customer_name and customer_phone and customer_address:

        st.session_state.customer = Customer(
            customer_name,
            customer_phone,
            customer_address,
        )

        st.success(
            f"Welcome, {customer_name}! Your profile is ready."
        )

    else:
        st.warning(
            "Please enter your name, phone and address."
        )


if st.session_state.customer:

    customer = st.session_state.customer

    st.markdown(
        f"""
        <div class="premium-card">
            <div class="card-icon">👋</div>

            <div class="card-title">
                Welcome, {customer._name}
            </div>

            <div class="card-text">
                📞 {customer._phone}<br>
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
        Add money to your wallet and use it for your order.
    </div>
    """,
    unsafe_allow_html=True,
)


wallet_col1, wallet_col2 = st.columns([2, 1])

with wallet_col1:

    wallet_amount = st.number_input(
        "Amount to add",
        min_value=0.0,
        step=100.0,
        format="%.2f",
    )

    if st.button(
        "＋ Add Money",
        use_container_width=True,
    ):

        if st.session_state.customer is None:

            st.warning(
                "Create a customer first."
            )

        elif wallet_amount <= 0:

            st.warning(
                "Enter an amount greater than ₹0."
            )

        else:

            st.session_state.customer.add_to_wallet(
                wallet_amount
            )

            st.success(
                f"₹{wallet_amount:.2f} added successfully!"
            )


with wallet_col2:

    if st.session_state.customer:

        balance = (
            st.session_state.customer._wallet_balance
        )

        st.markdown(
            f"""
            <div class="stat-card"
                 style="height:100%;">

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

    else:

        st.markdown(
            """
            <div class="stat-card"
                 style="height:100%;">

                <div class="stat-label">
                    Available Balance
                </div>

                <div class="stat-value">
                    ₹0.00
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
        Freshly prepared favorites
    </div>
    """,
    unsafe_allow_html=True,
)


menu_items = restaurant.get_menu()

food_emojis = {
    "Veg Burger": "🍔",
    "Pizza": "🍕",
    "Paneer Wrap": "🌯",
    "Chicken Biryani": "🍗",
    "French Fries": "🍟",
}


# Display menu in 3-column grid

for i in range(0, len(menu_items), 3):

    cols = st.columns(3)

    for j, col in enumerate(cols):

        index = i + j

        if index >= len(menu_items):
            break

        item = menu_items[index]

        emoji = food_emojis.get(
            item.name,
            "🍽️",
        )

        food_type = (
            "Veg"
            if item.is_veg
            else "Non-Veg"
        )

        badge_class = (
            "veg-badge"
            if item.is_veg
            else "nonveg-badge"
        )

        with col:

            st.markdown(
                f"""
                <div class="food-card">

                    <div style="
                        display:flex;
                        gap:15px;
                        align-items:center;
                    ">

                        <div class="food-emoji">
                            {emoji}
                        </div>

                        <div>
                            <div class="food-name">
                                {item.name}
                            </div>

                            <div class="food-price">
                                ₹{item.price:.2f}
                            </div>

                            <div class="{badge_class}">
                                {food_type}
                            </div>
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


st.divider()


# ============================================================
# ORDER SECTION
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🛒 Build Your Order
    </div>

    <div class="section-subtitle">
        Select your favorite items and review your bill.
    </div>
    """,
    unsafe_allow_html=True,
)


item_names = [
    item.name
    for item in restaurant.get_menu()
]


selected_items = st.multiselect(
    "Select food items",
    item_names,
    placeholder="Choose one or more items...",
)


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

    packaging = 20

    total = (
        subtotal
        + gst
        + packaging
    )

    order_col1, order_col2 = st.columns(
        [1.4, 1]
    )

    with order_col1:

        st.markdown(
            "### 🧾 Selected Items"
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
                    border:1px solid #eee;
                    border-radius:14px;
                    padding:13px 16px;
                    margin-bottom:8px;
                    display:flex;
                    justify-content:space-between;
                ">

                    <span>
                        {emoji}
                        &nbsp;
                        <b>{item.name}</b>
                    </span>

                    <span style="
                        color:#ff6b35;
                        font-weight:700;
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

                <div style="
                    font-size:18px;
                    font-weight:800;
                    margin-bottom:15px;
                ">
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

    if st.session_state.customer is None:

        st.warning(
            "Please create a customer first."
        )

    elif not selected_items:

        st.warning(
            "Select at least one food item."
        )

    else:

        selected_objects = [
            item
            for item in restaurant.get_menu()
            if item.name in selected_items
        ]

        order = (
            st.session_state.customer.place_order(
                restaurant,
                selected_objects,
            )
        )

        st.session_state.order = order

        st.success(
            f"🎉 Order #{order._order_id} placed successfully!"
        )

        st.markdown(
            f"""
            <div class="otp-card">

                <div class="otp-title">
                    🔐 YOUR DELIVERY OTP
                </div>

                <div class="otp-number">
                    {order._otp}
                </div>

                <div style="
                    color:#888;
                    font-size:11px;
                    margin-top:8px;
                ">
                    Demo OTP — shown for project purposes
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


st.divider()


# ============================================================
# ORDER STATUS
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

    c1, c2, c3 = st.columns(3)

    with c1:

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

    with c2:

        st.markdown(
            f"""
            <div class="stat-card">

                <div class="stat-label">
                    Current Status
                </div>

                <div style="
                    margin-top:10px;
                ">
                    <span class="status-badge">
                        {order._status}
                    </span>
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:

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


    # Progress indicator

    status = order._status

    statuses = [
        "Order Placed",
        "Order Accepted",
        "Delivered",
    ]

    status_index = 0

    if status == "Order Accepted":
        status_index = 1

    elif status == "Delivered":
        status_index = 2

    progress_cols = st.columns(3)

    for i, status_name in enumerate(statuses):

        with progress_cols[i]:

            if i <= status_index:

                icon = "🟢"

            else:

                icon = "⚪"

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    padding:15px;
                    background:white;
                    border-radius:15px;
                    border:1px solid #eee;
                ">

                    <div style="
                        font-size:24px;
                    ">
                        {icon}
                    </div>

                    <div style="
                        font-size:12px;
                        font-weight:700;
                        margin-top:7px;
                    ">
                        {status_name}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


else:

    st.markdown(
        """
        <div class="premium-card">

            <div class="card-icon">
                📦
            </div>

            <div class="card-title">
                No active order
            </div>

            <div class="card-text">
                Your order will appear here once
                you place your first order.
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
        Assign a delivery partner to your order.
    </div>
    """,
    unsafe_allow_html=True,
)


partner_col1, partner_col2, partner_col3 = st.columns(3)

with partner_col1:

    partner_name = st.text_input(
        "Partner Name",
        placeholder="Enter partner name",
    )

with partner_col2:

    partner_phone = st.text_input(
        "Partner Phone",
        placeholder="Enter phone number",
    )

with partner_col3:

    vehicle = st.selectbox(
        "Vehicle",
        [
            "Bike",
            "Scooter",
            "Cycle",
        ],
    )


if st.button(
    "🛵 Create Delivery Partner",
    use_container_width=True,
):

    if partner_name and partner_phone:

        st.session_state.delivery_partner = (
            DeliveryPartner(
                partner_name,
                partner_phone,
                vehicle,
            )
        )

        st.success(
            f"{partner_name} is ready for delivery."
        )

    else:

        st.warning(
            "Please enter partner name and phone."
        )


if st.session_state.delivery_partner:

    partner = (
        st.session_state.delivery_partner
    )

    partner_status = (
        "Available"
        if partner.is_available
        else "Busy"
    )

    st.markdown(
        f"""
        <div class="premium-card">

            <div style="
                display:flex;
                align-items:center;
                gap:18px;
            ">

                <div class="food-emoji">
                    🛵
                </div>

                <div>

                    <div class="card-title">
                        {partner._name}
                    </div>

                    <div class="card-text">
                        📞 {partner._phone}<br>
                        🛵 {partner.vehicle}
                    </div>

                </div>

                <div style="
                    margin-left:auto;
                    text-align:right;
                ">

                    <div class="stat-label">
                        STATUS
                    </div>

                    <div style="
                        color:#198754;
                        font-weight:800;
                        margin-top:5px;
                    ">
                        {partner_status}
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
        📦 Delivery Assignment
    </div>

    <div class="section-subtitle">
        Allow the delivery partner to accept the order.
    </div>
    """,
    unsafe_allow_html=True,
)


if st.button(
    "✅ Accept Order",
    type="primary",
    use_container_width=True,
):

    if st.session_state.order is None:

        st.warning(
            "Place an order first."
        )

    elif st.session_state.delivery_partner is None:

        st.warning(
            "Create a delivery partner first."
        )

    elif not st.session_state.delivery_partner.is_available:

        st.warning(
            "The delivery partner is already busy."
        )

    else:

        st.session_state.delivery_partner.accept_order(
            st.session_state.order
        )

        st.success(
            "🛵 Order accepted by delivery partner!"
        )


st.divider()


# ============================================================
# OTP DELIVERY
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🔐 Verify & Complete Delivery
    </div>

    <div class="section-subtitle">
        Enter the customer's OTP to complete the delivery.
    </div>
    """,
    unsafe_allow_html=True,
)


otp_col1, otp_col2 = st.columns(
    [2, 1]
)

with otp_col1:

    otp = st.number_input(
        "Enter 4-digit delivery OTP",
        min_value=1000,
        max_value=9999,
        step=1,
    )

with otp_col2:

    st.markdown(
        """
        <div class="premium-card"
             style="margin-top:28px;">

            <div style="
                font-size:12px;
                color:#888;
            ">
                SECURITY
            </div>

            <div style="
                font-weight:750;
                margin-top:5px;
            ">
                🔒 OTP Protected
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


if st.button(
    "🎉 Complete Delivery",
    type="primary",
    use_container_width=True,
):

    if st.session_state.order is None:

        st.warning(
            "No order available."
        )

    elif st.session_state.delivery_partner is None:

        st.warning(
            "Create a delivery partner first."
        )

    elif (
        st.session_state.order._status
        != "Order Accepted"
    ):

        st.warning(
            "The order must be accepted before delivery."
        )

    else:

        success = (
            st.session_state.delivery_partner.deliver(
                st.session_state.order,
                int(otp),
            )
        )

        if success:

            st.balloons()

            st.success(
                f"🎉 Order #{st.session_state.order._order_id} "
                "delivered successfully!"
            )

        else:

            st.error(
                "❌ Invalid OTP. Delivery not completed."
            )


st.divider()


# ============================================================
# FINAL RECEIPT
# ============================================================

st.markdown(
    """
    <div class="section-title">
        🧾 Final Receipt
    </div>

    <div class="section-subtitle">
        Your complete order summary.
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

        st.markdown(
            f"""
            <div class="premium-card">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                    margin-bottom:20px;
                ">

                    <div>
                        <div class="card-title">
                            Food Corner
                        </div>

                        <div class="card-text">
                            📍 {restaurant.location}
                        </div>
                    </div>

                    <div class="status-badge">
                        {order._status}
                    </div>

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
                            {
                                st.session_state.customer._name
                                if st.session_state.customer
                                else "Guest"
                            }
                        </b>

                    </div>

                    <div style="
                        display:flex;
                        justify-content:space-between;
                    ">

                        <span style="color:#777;">
                            Total Paid
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

            delivery_name = partner._name
            delivery_vehicle = partner.vehicle

        else:

            delivery_name = "Not assigned"
            delivery_vehicle = "-"


        st.markdown(
            f"""
            <div class="premium-card">

                <div class="card-icon">
                    🛵
                </div>

                <div class="card-title">
                    Delivery Details
                </div>

                <div class="card-text">

                    <b>Partner</b><br>
                    {delivery_name}

                    <br><br>

                    <b>Vehicle</b><br>
                    {delivery_vehicle}

                    <br><br>

                    <b>Restaurant</b><br>
                    {restaurant.name}

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

else:

    st.markdown(
        """
        <div class="premium-card">

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
                    Your receipt will appear here
                </div>

                <div class="card-text">
                    Place an order to generate
                    your final receipt.
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

        🍔 <b>Foodie</b> · Food Delivery OOP Project

        <br><br>

        Built with Python · Object-Oriented Programming · Streamlit

        <br>

        © 2026 Foodie. Demo project.

    </div>
    """,
    unsafe_allow_html=True,
)
