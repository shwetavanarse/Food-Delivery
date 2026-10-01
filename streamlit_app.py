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

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --orange: #ff6b35;
    --orange-dark: #e95420;
    --dark: #171717;
    --dark-2: #242424;
    --cream: #fff8f4;
    --bg: #f6f7f9;
    --border: #e8e8e8;
    --text: #1b1b1b;
    --muted: #747474;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: var(--bg);
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit default chrome */
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
    background: linear-gradient(180deg, #151515 0%, #222 100%);
}

section[data-testid="stSidebar"] * {
    color: white;
}

section[data-testid="stSidebar"] hr {
    border-color: #444;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    min-height: 44px;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* Primary buttons */
.stButton > button[kind="primary"] {
    background: linear-gradient(
        135deg,
        #ff6330,
        #ff8257
    );
    color: white;
    border: none;
}

/* Inputs */
.stTextInput input,
.stNumberInput input {
    border-radius: 11px !important;
    border: 1px solid #dedede !important;
}

div[data-baseweb="select"] > div {
    border-radius: 11px !important;
}

/* Multiselect */
div[data-baseweb="select"] {
    border-radius: 11px;
}

/* Tabs */
button[data-baseweb="tab"] {
    font-weight: 700;
}

/* Expander */
details {
    border-radius: 14px !important;
    border: 1px solid #e6e6e6 !important;
    background: white !important;
}

/* Success / warning boxes */
div[data-testid="stAlert"] {
    border-radius: 12px;
}


/* =========================================================
   HERO
   ========================================================= */

.hero-box {
    background:
        radial-gradient(
            circle at 85% 20%,
            rgba(255,107,53,0.25),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #141414 0%,
            #202020 55%,
            #382017 100%
        );

    border-radius: 28px;
    padding: 42px 48px;
    margin-bottom: 28px;
    min-height: 245px;
    position: relative;
    overflow: hidden;
    color: white;
}

.hero-box::after {
    content: "🍕";
    position: absolute;
    right: 45px;
    bottom: -25px;
    font-size: 170px;
    opacity: 0.10;
    transform: rotate(-12deg);
}

.hero-small {
    color: #ff9470;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 45px;
    font-weight: 800;
    line-height: 1.05;
    margin-bottom: 12px;
}

.hero-title span {
    color: #ff7040;
}

.hero-description {
    color: #c6c6c6;
    max-width: 600px;
    line-height: 1.6;
    font-size: 14px;
}


/* =========================================================
   SECTION
   ========================================================= */

.section-heading {
    font-size: 26px;
    font-weight: 800;
    color: var(--text);
    margin-top: 12px;
    margin-bottom: 3px;
}

.section-description {
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 20px;
}


/* =========================================================
   STAT CARDS
   ========================================================= */

.stat-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 20px;
    min-height: 110px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.035);
}

.stat-label {
    color: #8a8a8a;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.stat-value {
    color: #1c1c1c;
    font-size: 20px;
    font-weight: 800;
    margin-top: 9px;
}


/* =========================================================
   FOOD CARDS
   ========================================================= */

.food-card {
    background: white;
    border: 1px solid #e8e8e8;
    border-radius: 20px;
    padding: 19px;
    min-height: 185px;
    margin-bottom: 8px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.035);
}

.food-image {
    height: 72px;
    width: 72px;
    border-radius: 20px;
    background: #fff0e9;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 38px;
    margin-bottom: 13px;
}

.food-name {
    font-size: 16px;
    font-weight: 800;
    color: #202020;
}

.food-price {
    color: var(--orange);
    font-size: 16px;
    font-weight: 800;
    margin-top: 5px;
}


/* =========================================================
   CUSTOM INFO CARD
   ========================================================= */

.info-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 23px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.035);
}


/* =========================================================
   BILL
   ========================================================= */

.bill-card {
    background: linear-gradient(
        145deg,
        #171717,
        #292929
    );

    color: white;
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.12);
}

.bill-heading {
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 18px;
}

.bill-row {
    display: flex;
    justify-content: space-between;
    padding: 7px 0;
    color: #c8c8c8;
    font-size: 13px;
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

.bill-total-right {
    color: #ff8257;
}


/* =========================================================
   OTP
   ========================================================= */

.otp-box {
    background: linear-gradient(
        135deg,
        #fff1eb,
        #ffffff
    );
    border: 1px solid #ffd5c5;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
}

.otp-label {
    font-size: 10px;
    font-weight: 800;
    color: #888;
    letter-spacing: 1.5px;
}

.otp-value {
    color: var(--orange);
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 8px;
    margin-top: 5px;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer-box {
    text-align: center;
    color: #929292;
    font-size: 11px;
    padding-top: 35px;
}

</style>
""")


# ============================================================
# SESSION STATE
# ============================================================

if "customer" not in st.session_state:
    st.session_state.customer = None

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

if "delivery_partner" not in st.session_state:
    st.session_state.delivery_partner = None


restaurant = st.session_state.restaurant
menu = restaurant.get_menu()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;padding:15px 0 20px;">

            <div style="font-size:50px;">
                🍔
            </div>

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
        """
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

st.html("""
<div class="hero-box">

    <div class="hero-small">
        ✦ SMART FOOD DELIVERY SYSTEM
    </div>

    <div class="hero-title">
        Delicious food.<br>
        <span>Delivered simply.</span>
    </div>

    <div class="hero-description">
        Order your favourite meals, manage your wallet,
        assign a delivery partner and complete the delivery
        with OTP verification — all powered by Python OOP.
    </div>

</div>
""")


# ============================================================
# TOP STATS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.html(f"""
    <div class="stat-card">
        <div class="stat-label">Restaurant</div>
        <div class="stat-value">🍽️ Food Hub</div>
    </div>
    """)


with col2:
    st.html(f"""
    <div class="stat-card">
        <div class="stat-label">Menu Items</div>
        <div class="stat-value">{len(menu)} Items</div>
    </div>
    """)


with col3:

    customer_status = (
        "Active"
        if st.session_state.customer
        else "Not Created"
    )

    st.html(f"""
    <div class="stat-card">
        <div class="stat-label">Customer</div>
        <div class="stat-value">{customer_status}</div>
    </div>
    """)


with col4:

    if st.session_state.order:
        order_status = st.session_state.order._status
    else:
        order_status = "No Order"

    st.html(f"""
    <div class="stat-card">
        <div class="stat-label">Order Status</div>
        <div class="stat-value">{order_status}</div>
    </div>
    """)


st.divider()


# ============================================================
# CUSTOMER
# ============================================================

st.markdown(
    '<div class="section-heading">👤 Your Profile</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Create your customer profile to start ordering.'
    '</div>',
    unsafe_allow_html=True
)


with st.form("customer_form"):

    c1, c2, c3 = st.columns(3)

    with c1:
        name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )

    with c2:
        phone = st.text_input(
            "Phone Number",
            placeholder="Enter phone number"
        )

    with c3:
        address = st.text_input(
            "Delivery Address",
            placeholder="Enter delivery address"
        )

    create_customer = st.form_submit_button(
        "Create Customer",
        type="primary",
        use_container_width=True
    )


if create_customer:

    if name and phone and address:

        st.session_state.customer = Customer(
            name,
            phone,
            address
        )

        st.success(
            f"Welcome, {name}! Your profile has been created."
        )

    else:

        st.warning(
            "Please fill in all customer details."
        )


if st.session_state.customer:

    customer = st.session_state.customer

    st.info(
        f"👋 Welcome **{customer._name}**  ·  "
        f"📍 {customer._address}"
    )


st.divider()


# ============================================================
# WALLET
# ============================================================

st.markdown(
    '<div class="section-heading">💰 Wallet</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Add money to your wallet before placing an order.'
    '</div>',
    unsafe_allow_html=True
)


wallet1, wallet2 = st.columns([1.4, 1])


with wallet1:

    if st.session_state.customer:

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

            if amount > 0:

                st.session_state.customer.add_to_wallet(
                    amount
                )

                st.success(
                    f"₹{amount:.2f} added successfully."
                )

            else:

                st.warning(
                    "Enter an amount greater than zero."
                )

    else:

        st.info(
            "Create a customer first."
        )


with wallet2:

    balance = 0

    if st.session_state.customer:
        balance = (
            st.session_state.customer._wallet_balance
        )

    st.html(f"""
    <div class="stat-card">

        <div class="stat-label">
            AVAILABLE BALANCE
        </div>

        <div class="stat-value"
             style="color:#ff6b35;font-size:28px;">
            ₹{balance:.2f}
        </div>

    </div>
    """)


st.divider()


# ============================================================
# MENU
# ============================================================

st.markdown(
    '<div class="section-heading">🍽️ Explore Our Menu</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Fresh favourites available at Food Hub.'
    '</div>',
    unsafe_allow_html=True
)


food_icons = {
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

        icon = food_icons.get(
            item.name,
            "🍽️"
        )

        food_type = (
            "🟢 Veg"
            if item.is_veg
            else "🔴 Non-Veg"
        )

        with col:

            st.html(f"""
            <div class="food-card">

                <div class="food-image">
                    {icon}
                </div>

                <div class="food-name">
                    {item.name}
                </div>

                <div class="food-price">
                    ₹{item.price:.2f}
                </div>

                <div style="
                    color:#777;
                    font-size:10px;
                    margin-top:7px;
                    font-weight:700;
                ">
                    {food_type}
                </div>

            </div>
            """)


st.divider()


# ============================================================
# ORDER
# ============================================================

st.markdown(
    '<div class="section-heading">🛒 Build Your Order</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Select your favourite items and review your bill.'
    '</div>',
    unsafe_allow_html=True
)


if st.session_state.customer:

    selected = st.multiselect(
        "Choose food items",
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

        order_left, order_right = st.columns(
            [1.3, 1]
        )

        with order_left:

            st.markdown("#### 🍴 Your Selection")

            for item in selected_items:

                icon = food_icons.get(
                    item.name,
                    "🍽️"
                )

                st.write(
                    f"{icon} **{item.name}**  "
                    f"— ₹{item.price:.2f}"
                )

        with order_right:

            st.html(f"""
            <div class="bill-card">

                <div class="bill-heading">
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
                    <span class="bill-total-right">
                        ₹{total:.2f}
                    </span>
                </div>

            </div>
            """)

        st.write("")

        if st.button(
            "🛍️ Place Order",
            type="primary",
            use_container_width=True
        ):

            items = [
                item
                for item in menu
                if item.name in selected
            ]

            st.session_state.order = (
                st.session_state.customer.place_order(
                    restaurant,
                    items
                )
            )

            order = st.session_state.order

            st.success(
                f"🎉 Order #{order._order_id} placed successfully!"
            )

            st.html("""
            <div class="otp-box">

                <div class="otp-label">
                    DEMO DELIVERY OTP
                </div>

                <div class="otp-value">
                    1234
                </div>

                <div style="
                    color:#888;
                    font-size:10px;
                    margin-top:5px;
                ">
                    Project demonstration OTP
                </div>

            </div>
            """)

    else:

        st.info(
            "Choose at least one item to continue."
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
    '<div class="section-heading">📦 Track Your Order</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Monitor your order as it moves towards delivery.'
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

    st.write("")

    st.progress(
        0.33
        if order._status != "Delivered"
        else 1.0
    )

    if order._status == "Delivered":

        st.success(
            "🎉 Your order has been delivered!"
        )

    elif order._status == "Order Accepted":

        st.info(
            "🛵 Your delivery partner has accepted the order."
        )

    else:

        st.info(
            "🍳 Your order has been placed and is being prepared."
        )

else:

    st.info(
        "No active order yet."
    )


st.divider()


# ============================================================
# DELIVERY PARTNER
# ============================================================

st.markdown(
    '<div class="section-heading">🛵 Delivery Partner</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Assign a delivery partner to your order.'
    '</div>',
    unsafe_allow_html=True
)


with st.form("delivery_form"):

    d1, d2, d3 = st.columns(3)

    with d1:
        dp_name = st.text_input(
            "Partner Name",
            placeholder="Enter partner name"
        )

    with d2:
        dp_phone = st.text_input(
            "Partner Phone",
            placeholder="Enter phone number"
        )

    with d3:
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
        type="primary",
        use_container_width=True
    )


if create_partner:

    if dp_name and dp_phone:

        st.session_state.delivery_partner = (
            DeliveryPartner(
                dp_name,
                dp_phone,
                vehicle
            )
        )

        st.success(
            f"🛵 {dp_name} is now available."
        )

    else:

        st.warning(
            "Please enter partner name and phone."
        )


if st.session_state.delivery_partner:

    partner = st.session_state.delivery_partner

    st.info(
        f"🛵 **{partner._name}**  ·  "
        f"{partner.vehicle}  ·  "
        f"{'Available' if partner.is_available else 'Busy'}"
    )


st.divider()


# ============================================================
# ACCEPT ORDER
# ============================================================

st.markdown(
    '<div class="section-heading">📦 Accept Order</div>',
    unsafe_allow_html=True
)

if (
    st.session_state.order
    and st.session_state.delivery_partner
):

    if st.button(
        "✅ Accept Order",
        type="primary",
        use_container_width=True
    ):

        st.session_state.delivery_partner.accept_order(
            st.session_state.order
        )

        st.success(
            "🛵 Order accepted by delivery partner."
        )

else:

    st.info(
        "Create an order and delivery partner first."
    )


st.divider()


# ============================================================
# OTP
# ============================================================

st.markdown(
    '<div class="section-heading">🔐 Delivery Verification</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Verify the customer OTP before completing delivery.'
    '</div>',
    unsafe_allow_html=True
)


if st.session_state.order:

    st.html("""
    <div class="otp-box">

        <div class="otp-label">
            DEMO OTP
        </div>

        <div class="otp-value">
            1234
        </div>

    </div>
    """)

    otp = st.number_input(
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

        if st.session_state.order.verify_otp(otp):

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
    '<div class="section-heading">🎉 Complete Delivery</div>',
    unsafe_allow_html=True
)


if (
    st.session_state.order
    and st.session_state.delivery_partner
):

    delivery_otp = st.number_input(
        "Enter delivery OTP",
        min_value=0,
        max_value=9999,
        step=1,
        key="complete_delivery_otp"
    )

    if st.button(
        "🎉 Complete Delivery",
        type="primary",
        use_container_width=True
    ):

        # Verify first
        verified = (
            st.session_state.order.verify_otp(
                delivery_otp
            )
        )

        if verified:

            result = (
                st.session_state.delivery_partner.deliver(
                    st.session_state.order,
                    delivery_otp
                )
            )

            st.balloons()

            st.success(
                "🎉 Delivery completed successfully!"
            )

        else:

            st.error(
                "❌ Incorrect OTP. Delivery not completed."
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
    '<div class="section-heading">🧾 Order Summary</div>',
    unsafe_allow_html=True
)


if st.session_state.order:

    order = st.session_state.order

    summary1, summary2 = st.columns(2)

    with summary1:

        st.html(f"""
        <div class="info-card">

            <h3>🍔 Order Details</h3>

            <p>
                <b>Order ID:</b>
                #{order._order_id}
            </p>

            <p>
                <b>Status:</b>
                {order._status}
            </p>

            <p>
                <b>Estimated Time:</b>
                {order.estimated_time()} minutes
            </p>

            <p>
                <b>Total Bill:</b>
                ₹{order.calculate_bill():.2f}
            </p>

        </div>
        """)

    with summary2:

        if st.session_state.delivery_partner:

            partner = st.session_state.delivery_partner

            partner_text = partner._name
            vehicle_text = partner.vehicle

        else:

            partner_text = "Not assigned"
            vehicle_text = "-"

        st.html(f"""
        <div class="info-card">

            <h3>🛵 Delivery Details</h3>

            <p>
                <b>Partner:</b>
                {partner_text}
            </p>

            <p>
                <b>Vehicle:</b>
                {vehicle_text}
            </p>

            <p>
                <b>Restaurant:</b>
                {restaurant.name}
            </p>

            <p>
                <b>Location:</b>
                {restaurant.location}
            </p>

        </div>
        """)

else:

    st.info(
        "Your final order summary will appear here."
    )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer-box">

    🍔 <b>Foodie</b> · OOP Food Delivery System

    <br><br>

    Built with Python · Object-Oriented Programming · Streamlit

    <br>

    © 2026 Foodie Portfolio Project

</div>
""")
