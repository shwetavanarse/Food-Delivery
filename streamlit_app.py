```python
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
# PREMIUM STYLING
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f7f7f8;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
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

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #151515, #242424);
}

section[data-testid="stSidebar"] * {
    color: white;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    min-height: 44px;
    font-weight: 700;
    transition: 0.2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* Primary button */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #ff6330, #ff8a62);
    color: white;
    border: none;
}

/* Inputs */
.stTextInput input,
.stNumberInput input {
    border-radius: 11px !important;
}

div[data-baseweb="select"] > div {
    border-radius: 11px !important;
}

/* Hero */
.hero {
    background:
        radial-gradient(
            circle at 88% 25%,
            rgba(255,107,53,0.25),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #151515,
            #252525 60%,
            #382017
        );

    border-radius: 28px;
    padding: 45px 50px;
    margin-bottom: 30px;
    min-height: 230px;
    position: relative;
    overflow: hidden;
    color: white;
    box-shadow: 0 20px 50px rgba(0,0,0,0.12);
}

.hero:after {
    content: "🍕";
    position: absolute;
    right: 45px;
    bottom: -25px;
    font-size: 170px;
    opacity: 0.10;
    transform: rotate(-12deg);
}

.hero-badge {
    color: #ff936d;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 44px;
    font-weight: 800;
    line-height: 1.05;
}

.hero-title span {
    color: #ff7040;
}

.hero-text {
    color: #c9c9c9;
    max-width: 620px;
    margin-top: 15px;
    font-size: 14px;
    line-height: 1.6;
}

/* Section titles */
.section-title {
    font-size: 26px;
    font-weight: 800;
    color: #191919;
    margin-top: 8px;
}

.section-subtitle {
    color: #777;
    font-size: 13px;
    margin-bottom: 20px;
}

/* Cards */
.card {
    background: white;
    border: 1px solid #e9e9e9;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 7px 25px rgba(0,0,0,0.04);
}

.card-title {
    font-size: 17px;
    font-weight: 800;
    color: #202020;
}

.card-text {
    color: #777;
    font-size: 13px;
    line-height: 1.7;
    margin-top: 8px;
}

/* Stats */
.stat {
    background: white;
    border: 1px solid #e9e9e9;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.035);
}

.stat-label {
    color: #888;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stat-value {
    color: #1b1b1b;
    font-size: 22px;
    font-weight: 800;
    margin-top: 8px;
}

/* Food */
.food-card {
    background: white;
    border: 1px solid #e9e9e9;
    border-radius: 20px;
    padding: 20px;
    min-height: 175px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.035);
}

.food-icon {
    width: 65px;
    height: 65px;
    border-radius: 18px;
    background: #fff1eb;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 34px;
    margin-bottom: 13px;
}

.food-name {
    font-size: 16px;
    font-weight: 800;
}

.food-price {
    color: #ff6b35;
    font-size: 16px;
    font-weight: 800;
    margin-top: 5px;
}

.food-type {
    color: #777;
    font-size: 10px;
    font-weight: 700;
    margin-top: 6px;
}

/* Bill */
.bill {
    background: linear-gradient(145deg, #171717, #292929);
    color: white;
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.12);
}

.bill-title {
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 15px;
}

.bill-row {
    display: flex;
    justify-content: space-between;
    color: #ccc;
    font-size: 13px;
    padding: 7px 0;
}

.bill-total {
    border-top: 1px solid #444;
    margin-top: 12px;
    padding-top: 15px;
    display: flex;
    justify-content: space-between;
    font-size: 20px;
    font-weight: 800;
}

.bill-total span:last-child {
    color: #ff8257;
}

/* OTP */
.otp {
    background: linear-gradient(135deg, #fff1eb, #ffffff);
    border: 1px solid #ffd5c5;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
}

.otp-label {
    color: #888;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.otp-number {
    color: #ff6b35;
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 8px;
    margin-top: 6px;
}

/* Footer */
.footer {
    text-align: center;
    color: #999;
    font-size: 11px;
    padding-top: 35px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "customer" not in st.session_state:
    st.session_state.customer = None

if "delivery_partner" not in st.session_state:
    st.session_state.delivery_partner = None

if "restaurant" not in st.session_state:

    restaurant = Restaurant(
        "Food Hub",
        "Sambhajinagar"
    )

    restaurant.add_item(
        MenuItem("Veg Burger", 120, True)
    )

    restaurant.add_item(
        MenuItem("Pizza", 250, True)
    )

    restaurant.add_item(
        MenuItem("French Fries", 100, True)
    )

    restaurant.add_item(
        MenuItem("Cold Drink", 60, True)
    )

    st.session_state.restaurant = restaurant

if "order" not in st.session_state:
    st.session_state.order = None


restaurant = st.session_state.restaurant
menu = restaurant.get_menu()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;padding:15px 0 20px;">
            <div style="font-size:50px;">🍔</div>

            <div style="
                font-size:27px;
                font-weight:800;
            ">
                Foodie
            </div>

            <div style="
                color:#aaa;
                font-size:11px;
                margin-top:5px;
            ">
                SMART FOOD DELIVERY
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🍽️ Restaurant")

    st.caption(
        f"{restaurant.name} · {restaurant.location}"
    )

    st.divider()

    st.markdown("### 🚀 Order Journey")

    st.markdown(
        """
        👤 Customer Profile

        💰 Wallet

        🍽️ Menu

        🛒 Place Order

        🛵 Delivery Partner

        📦 Accept Order

        🔐 OTP Verification

        🎉 Complete Delivery
        """
    )

    if st.session_state.customer:

        st.divider()

        customer = st.session_state.customer

        st.markdown("### 👤 Customer")

        st.write(customer._name)

        st.caption(
            f"Wallet: ₹{customer._wallet_balance:.2f}"
        )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            ✦ SMART FOOD DELIVERY SYSTEM
        </div>

        <div class="hero-title">
            Delicious food.<br>
            <span>Delivered simply.</span>
        </div>

        <div class="hero-text">
            Order your favourite meals, manage your wallet,
            assign a delivery partner and complete delivery
            with OTP verification — powered by Python OOP.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TOP STATS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="stat">
            <div class="stat-label">Restaurant</div>
            <div class="stat-value">🍽️ {restaurant.name}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="stat">
            <div class="stat-label">Menu Items</div>
            <div class="stat-value">{len(menu)} Items</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    customer_status = (
        "Active"
        if st.session_state.customer
        else "Not Created"
    )

    st.markdown(
        f"""
        <div class="stat">
            <div class="stat-label">Customer</div>
            <div class="stat-value">{customer_status}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:

    order_status = (
        st.session_state.order._status
        if st.session_state.order
        else "No Order"
    )

    st.markdown(
        f"""
        <div class="stat">
            <div class="stat-label">Order Status</div>
            <div class="stat-value">{order_status}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# CUSTOMER
# ============================================================

st.markdown(
    '<div class="section-title">👤 Your Profile</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Create your customer profile to start ordering.'
    '</div>',
    unsafe_allow_html=True
)


c1, c2, c3 = st.columns(3)

with c1:
    customer_name = st.text_input(
        "Full Name",
        placeholder="Enter your name"
    )

with c2:
    customer_phone = st.text_input(
        "Phone Number",
        placeholder="Enter phone number"
    )

with c3:
    customer_address = st.text_input(
        "Delivery Address",
        placeholder="Enter delivery address"
    )


if st.button(
    "Create Customer",
    type="primary",
    use_container_width=True
):

    if customer_name and customer_phone and customer_address:

        st.session_state.customer = Customer(
            customer_name,
            customer_phone,
            customer_address
        )

        st.success(
            f"Welcome, {customer_name}! Your profile is ready."
        )

    else:

        st.warning(
            "Please enter name, phone and address."
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
                📞 {customer._phone}<br>
                📍 {customer.address}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# WALLET
# ============================================================

st.markdown(
    '<div class="section-title">💰 Wallet</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Add money to your wallet before ordering.'
    '</div>',
    unsafe_allow_html=True
)


wallet_left, wallet_right = st.columns([2, 1])

with wallet_left:

    amount = st.number_input(
        "Amount to Add (₹)",
        min_value=0.0,
        step=50.0,
        format="%.2f"
    )

    if st.button(
        "＋ Add Money",
        use_container_width=True
    ):

        if st.session_state.customer is None:

            st.warning(
                "Create a customer first."
            )

        elif amount <= 0:

            st.warning(
                "Enter an amount greater than ₹0."
            )

        else:

            st.session_state.customer.add_to_wallet(
                amount
            )

            st.success(
                f"₹{amount:.2f} added to wallet."
            )


with wallet_right:

    balance = 0

    if st.session_state.customer:
        balance = (
            st.session_state.customer._wallet_balance
        )

    st.markdown(
        f"""
        <div class="stat">

            <div class="stat-label">
                Available Balance
            </div>

            <div class="stat-value"
                 style="color:#ff6b35;">
                ₹{balance:.2f}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# MENU
# ============================================================

st.markdown(
    '<div class="section-title">🍽️ Explore Our Menu</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Fresh favourites available at Food Hub.'
    '</div>',
    unsafe_allow_html=True
)


icons = {
    "Veg Burger": "🍔",
    "Pizza": "🍕",
    "French Fries": "🍟",
    "Cold Drink": "🥤",
    "Paneer Wrap": "🌯",
    "Chicken Biryani": "🍗",
}


for start in range(0, len(menu), 4):

    cols = st.columns(4)

    for i, col in enumerate(cols):

        index = start + i

        if index >= len(menu):
            continue

        item = menu[index]

        icon = icons.get(item.name, "🍽️")

        item_type = (
            "🟢 Veg"
            if item.is_veg
            else "🔴 Non-Veg"
        )

        with col:

            st.markdown(
                f"""
                <div class="food-card">

                    <div class="food-icon">
                        {icon}
                    </div>

                    <div class="food-name">
                        {item.name}
                    </div>

                    <div class="food-price">
                        ₹{item.price:.2f}
                    </div>

                    <div class="food-type">
                        {item_type}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


st.divider()


# ============================================================
# PLACE ORDER
# ============================================================

st.markdown(
    '<div class="section-title">🛒 Build Your Order</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Select your favourite dishes and review your bill.'
    '</div>',
    unsafe_allow_html=True
)


if st.session_state.customer:

    selected = st.multiselect(
        "Choose Food Items",
        [item.name for item in menu],
        placeholder="Select one or more dishes..."
    )

    if selected:

        selected_items = [
            item
            for item in menu
            if item.name in selected
        ]

        subtotal = sum(
            item.price
            for item in selected_items
        )

        gst = subtotal * 0.05
        packaging = 20
        total = subtotal + gst + packaging

        left, right = st.columns([1.2, 1])

        with left:

            st.markdown("### 🍴 Selected Items")

            for item in selected_items:

                icon = icons.get(
                    item.name,
                    "🍽️"
                )

                st.write(
                    f"{icon} **{item.name}** — "
                    f"₹{item.price:.2f}"
                )

        with right:

            st.markdown(
                f"""
                <div class="bill">

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
                unsafe_allow_html=True
            )

        st.write("")

        if st.button(
            "🛍️ Place Order",
            type="primary",
            use_container_width=True
        ):

            st.session_state.order = (
                st.session_state.customer.place_order(
                    restaurant,
                    selected_items
                )
            )

            order = st.session_state.order

            st.success(
                f"🎉 Order #{order._order_id} placed successfully!"
            )

            st.markdown(
                """
                <div class="otp">

                    <div class="otp-label">
                        DELIVERY OTP
                    </div>

                    <div class="otp-number">
                        1234
                    </div>

                    <div style="
                        color:#888;
                        font-size:10px;
                        margin-top:5px;
                    ">
                        Demo OTP for project presentation
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "Choose at least one food item."
        )

else:

    st.warning(
        "Create a customer before placing an order."
    )


st.divider()


# ============================================================
# ORDER STATUS
# ============================================================

st.markdown(
    '<div class="section-title">📦 Track Your Order</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Follow your order from placement to delivery.'
    '</div>',
    unsafe_allow_html=True
)


if st.session_state.order:

    order = st.session_state.order

    s1, s2, s3 = st.columns(3)

    with s1:
        st.metric(
            "Order ID",
            f"#{order._order_id}"
        )

    with s2:
        st.metric(
            "Status",
            order._status
        )

    with s3:
        st.metric(
            "Estimated Time",
            f"{order.estimated_time()} min"
        )

    status_progress = {
        "Placed": 0.33,
        "Accepted": 0.66,
        "Delivered": 1.0
    }

    st.progress(
        status_progress.get(
            order._status,
            0.33
        )
    )

    if order._status == "Placed":

        st.info(
            "🍳 Your order has been placed."
        )

    elif order._status == "Accepted":

        st.info(
            "🛵 Your delivery partner accepted the order."
        )

    elif order._status == "Delivered":

        st.success(
            "🎉 Your order has been delivered!"
        )

else:

    st.info(
        "No order placed yet."
    )


st.divider()


# ============================================================
# DELIVERY PARTNER
# ============================================================

st.markdown(
    '<div class="section-title">🛵 Delivery Partner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Create a delivery partner for the order.'
    '</div>',
    unsafe_allow_html=True
)


d1, d2, d3 = st.columns(3)

with d1:

    partner_name = st.text_input(
        "Partner Name",
        placeholder="Enter partner name"
    )

with d2:

    partner_phone = st.text_input(
        "Partner Phone",
        placeholder="Enter phone number"
    )

with d3:

    vehicle = st.selectbox(
        "Vehicle",
        ["Bike", "Scooter", "Car"]
    )


if st.button(
    "Create Delivery Partner",
    use_container_width=True
):

    if partner_name and partner_phone:

        st.session_state.delivery_partner = (
            DeliveryPartner(
                partner_name,
                partner_phone,
                vehicle
            )
        )

        st.success(
            f"🛵 {partner_name} is now available."
        )

    else:

        st.warning(
            "Enter partner name and phone."
        )


if st.session_state.delivery_partner:

    partner = st.session_state.delivery_partner

    availability = (
        "Available"
        if partner.is_available
        else "Busy"
    )

    st.markdown(
        f"""
        <div class="card">

            <div class="card-title">
                🛵 {partner._name}
            </div>

            <div class="card-text">
                📞 {partner._phone}<br>
                🚗 Vehicle: {partner.vehicle}<br>
                🟢 Status: {availability}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# ACCEPT ORDER
# ============================================================

st.markdown(
    '<div class="section-title">📦 Accept Order</div>',
    unsafe_allow_html=True
)


if (
    st.session_state.order
    and st.session_state.delivery_partner
):

    partner = st.session_state.delivery_partner
    order = st.session_state.order

    if order._status == "Placed":

        if partner.is_available:

            if st.button(
                "✅ Accept Order",
                type="primary",
                use_container_width=True
            ):

                partner.accept_order(order)

                st.success(
                    "🛵 Order accepted by delivery partner!"
                )

        else:

            st.warning(
                "Delivery partner is currently busy."
            )

    elif order._status == "Accepted":

        st.info(
            "Order has already been accepted."
        )

    else:

        st.success(
            "Order has already been delivered."
        )

else:

    st.info(
        "Create an order and delivery partner first."
    )


st.divider()


# ============================================================
# OTP VERIFICATION
# ============================================================

st.markdown(
    '<div class="section-title">🔐 OTP Verification</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Verify the delivery OTP before completing the order.'
    '</div>',
    unsafe_allow_html=True
)


if st.session_state.order:

    st.markdown(
        """
        <div class="otp">

            <div class="otp-label">
                DEMO DELIVERY OTP
            </div>

            <div class="otp-number">
                1234
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    entered_otp = st.number_input(
        "Enter OTP",
        min_value=0,
        max_value=9999,
        step=1,
        key="verify_otp"
    )

    if st.button(
        "🔐 Verify OTP",
        use_container_width=True
    ):

        if st.session_state.order.verify_otp(
            int(entered_otp)
        ):

            st.success(
                "✅ OTP verified successfully!"
            )

        else:

            st.error(
                "❌ Incorrect OTP."
            )

else:

    st.info(
        "Place an order first."
    )


st.divider()


# ============================================================
# COMPLETE DELIVERY
# ============================================================

st.markdown(
    '<div class="section-title">🎉 Complete Delivery</div>',
    unsafe_allow_html=True
)


if (
    st.session_state.order
    and st.session_state.delivery_partner
):

    order = st.session_state.order
    partner = st.session_state.delivery_partner

    if order._status == "Accepted":

        delivery_otp = st.number_input(
            "Enter Delivery OTP",
            min_value=0,
            max_value=9999,
            step=1,
            key="delivery_otp"
        )

        if st.button(
            "🎉 Complete Delivery",
            type="primary",
            use_container_width=True
        ):

            if order.verify_otp(
                int(delivery_otp)
            ):

                partner.deliver(
                    order,
                    int(delivery_otp)
                )

                st.balloons()

                st.success(
                    f"🎉 Order #{order._order_id} "
                    "delivered successfully!"
                )

            else:

                st.error(
                    "❌ Invalid OTP. Delivery not completed."
                )

    elif order._status == "Delivered":

        st.success(
            "🎉 This order has already been delivered."
        )

    else:

        st.warning(
            "The order must be accepted before delivery."
        )

else:

    st.info(
        "Create an order and delivery partner first."
    )


st.divider()


# ============================================================
# FINAL SUMMARY
# ============================================================

st.markdown(
    '<div class="section-title">🧾 Final Order Summary</div>',
    unsafe_allow_html=True
)


if st.session_state.order:

    order = st.session_state.order

    summary_left, summary_right = st.columns(2)

    with summary_left:

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    🍔 Order Details
                </div>

                <div class="card-text">

                    <b>Order ID:</b>
                    #{order._order_id}<br>

                    <b>Status:</b>
                    {order._status}<br>

                    <b>Estimated Time:</b>
                    {order.estimated_time()} minutes<br>

                    <b>Total Bill:</b>
                    ₹{order.calculate_bill():.2f}

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with summary_right:

        if st.session_state.delivery_partner:

            partner = st.session_state.delivery_partner

            partner_name_display = partner._name
            vehicle_display = partner.vehicle

        else:

            partner_name_display = "Not Assigned"
            vehicle_display = "-"

        st.markdown(
            f"""
            <div class="card">

                <div class="card-title">
                    🛵 Delivery Details
                </div>

                <div class="card-text">

                    <b>Partner:</b>
                    {partner_name_display}<br>

                    <b>Vehicle:</b>
                    {vehicle_display}<br>

                    <b>Restaurant:</b>
                    {restaurant.name}<br>

                    <b>Location:</b>
                    {restaurant.location}

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

else:

    st.info(
        "Complete an order to see the final summary."
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

        © 2026 Foodie Portfolio Project

    </div>
    """,
    unsafe_allow_html=True
)
```
