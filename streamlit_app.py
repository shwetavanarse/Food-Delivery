import streamlit as st

from food_delivery import Customer, DeliveryPartner, MenuItem, Restaurant


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Food Delivery OOP",
    page_icon="🍔",
    layout="wide",
)


# ============================================================
# CUSTOM CSS — VISUAL CHANGES ONLY
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- Main page ---------- */

    .stApp {
        background: #fffaf7;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    /* ---------- Header ---------- */

    .main-title {
        background: linear-gradient(
            135deg,
            #ff6b35,
            #ff8f5c
        );
        color: white;
        padding: 28px 32px;
        border-radius: 18px;
        margin-bottom: 8px;
        box-shadow: 0 8px 25px rgba(255, 107, 53, 0.18);
    }

    .main-title h1 {
        margin: 0;
        font-size: 34px;
        font-weight: 800;
    }

    .main-title p {
        margin: 7px 0 0 0;
        font-size: 14px;
        opacity: 0.92;
    }

    /* ---------- Section headers ---------- */

    h2 {
        color: #222222 !important;
        font-weight: 750 !important;
        margin-top: 10px !important;
    }

    /* ---------- Input boxes ---------- */

    div[data-baseweb="input"] {
        border-radius: 10px;
    }

    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }

    /* ---------- Buttons ---------- */

    .stButton > button {
        border-radius: 10px;
        font-weight: 650;
        border: 1px solid #ff6b35;
        min-height: 42px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #e95725;
        transform: translateY(-1px);
        box-shadow: 0 5px 15px rgba(255, 107, 53, 0.15);
    }

    /* ---------- Metrics ---------- */

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #f0dfd8;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.035);
    }

    div[data-testid="stMetricLabel"] {
        color: #777777;
    }

    div[data-testid="stMetricValue"] {
        color: #ff6330;
        font-weight: 750;
    }

    /* ---------- Table ---------- */

    div[data-testid="stTable"] {
        background: white;
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid #f0dfd8;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.035);
    }

    /* ---------- Alerts ---------- */

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* ---------- Info cards ---------- */

    .info-card {
        background: white;
        border: 1px solid #f0dfd8;
        border-left: 5px solid #ff6b35;
        border-radius: 12px;
        padding: 15px 18px;
        margin: 8px 0 15px 0;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.035);
    }

    .info-title {
        color: #333333;
        font-weight: 700;
        font-size: 15px;
    }

    .info-text {
        color: #777777;
        font-size: 13px;
        margin-top: 5px;
    }

    /* ---------- Bill card ---------- */

    .bill-card {
        background: linear-gradient(
            135deg,
            #fff1ea,
            #fffaf7
        );
        border: 1px solid #ffd7c7;
        border-radius: 14px;
        padding: 18px;
        margin-top: 12px;
    }

    .bill-title {
        font-size: 16px;
        font-weight: 750;
        color: #333333;
        margin-bottom: 10px;
    }

    .bill-total {
        font-size: 22px;
        font-weight: 800;
        color: #ff6330;
    }

    /* ---------- Restaurant badge ---------- */

    .restaurant-badge {
        display: inline-block;
        background: #fff0e9;
        color: #e95725;
        padding: 7px 13px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    /* ---------- Footer ---------- */

    .footer {
        text-align: center;
        color: #999999;
        font-size: 12px;
        padding: 25px 0 5px 0;
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
# HEADER
# ============================================================

st.markdown(
    """
    <div class="main-title">
        <h1>🍔 Food Delivery System</h1>
        <p>
            A simple and interactive food delivery application
            built with Python OOP and Streamlit.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# RESTAURANT INFO
# ============================================================

st.markdown(
    f"""
    <div class="restaurant-badge">
        🍽️ {restaurant.name} &nbsp; • &nbsp; 📍 {restaurant.location}
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()


# ============================================================
# 1. CUSTOMER
# ============================================================

st.header("1. Create Customer")

col1, col2, col3 = st.columns(3)

with col1:
    customer_name = st.text_input(
        "Customer Name",
        placeholder="Enter your name",
    )

with col2:
    customer_phone = st.text_input(
        "Phone",
        placeholder="Enter phone number",
    )

with col3:
    customer_address = st.text_input(
        "Address",
        placeholder="Enter delivery address",
    )


if st.button(
    "👤 Create Customer",
    type="primary",
):

    if customer_name and customer_phone and customer_address:

        st.session_state.customer = Customer(
            customer_name,
            customer_phone,
            customer_address,
        )

        st.success(
            f"Customer '{customer_name}' created successfully!"
        )

    else:

        st.warning(
            "Please enter name, phone and address."
        )


if st.session_state.customer:

    customer = st.session_state.customer

    st.markdown(
        f"""
        <div class="info-card">

            <div class="info-title">
                👋 Customer Profile
            </div>

            <div class="info-text">
                <b>Name:</b> {customer._name}
                &nbsp; | &nbsp;
                <b>Wallet:</b>
                ₹{customer._wallet_balance:.2f}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# 2. WALLET
# ============================================================

st.header("2. Add Wallet Balance")

wallet_amount = st.number_input(
    "Amount",
    min_value=0.0,
    step=100.0,
    format="%.2f",
)


if st.button("💰 Add Money"):

    if st.session_state.customer is None:

        st.warning(
            "Create a customer first."
        )

    elif wallet_amount <= 0:

        st.warning(
            "Enter an amount greater than 0."
        )

    else:

        st.session_state.customer.add_to_wallet(
            wallet_amount
        )

        st.success(
            f"₹{wallet_amount:.2f} added to wallet."
        )


if st.session_state.customer:

    st.metric(
        "Current Wallet Balance",
        f"₹{st.session_state.customer._wallet_balance:.2f}",
    )


st.divider()


# ============================================================
# 3. RESTAURANT MENU
# ============================================================

st.header("3. Restaurant Menu")

st.write(
    f"**{restaurant.name}** — {restaurant.location}"
)

menu_data = []

for item in restaurant.get_menu():

    menu_data.append(
        {
            "🍽️ Item": item.name,
            "💰 Price": f"₹{item.price:.2f}",
            "🥗 Type": (
                "🟢 Veg"
                if item.is_veg
                else "🔴 Non-Veg"
            ),
        }
    )


st.table(menu_data)


st.divider()


# ============================================================
# 4. PLACE ORDER
# ============================================================

st.header("4. Place Order")

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
    total = subtotal + gst + packaging

    st.markdown(
        f"""
        <div class="bill-card">

            <div class="bill-title">
                🧾 Order Bill
            </div>

            <div>
                Subtotal:
                <b>₹{subtotal:.2f}</b>
            </div>

            <div>
                GST (5%):
                <b>₹{gst:.2f}</b>
            </div>

            <div>
                Packaging Fee:
                <b>₹{packaging:.2f}</b>
            </div>

            <hr>

            <div class="bill-total">
                Total: ₹{total:.2f}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


if st.button(
    "🛒 Place Order",
    type="primary",
):

    if st.session_state.customer is None:

        st.warning(
            "Create a customer first."
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

        order = st.session_state.customer.place_order(
            restaurant,
            selected_objects,
        )

        st.session_state.order = order

        st.success(
            f"Order #{order._order_id} placed successfully!"
        )

        st.warning(
            f"🔐 Delivery OTP: {order._otp} "
            "(shown here for project/demo purposes)"
        )


st.divider()


# ============================================================
# 5. ORDER STATUS
# ============================================================

st.header("5. Order Status")


if st.session_state.order:

    order = st.session_state.order

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Order ID",
            order._order_id,
        )

    with c2:

        st.metric(
            "Status",
            order._status,
        )

    with c3:

        st.metric(
            "Estimated Time",
            f"{order.estimated_time()} min",
        )

    st.write(
        f"**💳 Bill:** ₹{order.calculate_bill():.2f}"
    )

else:

    st.info(
        "No order has been placed yet."
    )


st.divider()


# ============================================================
# 6. DELIVERY PARTNER
# ============================================================

st.header("6. Create Delivery Partner")

col1, col2, col3 = st.columns(3)

with col1:

    partner_name = st.text_input(
        "Partner Name",
        placeholder="Enter partner name",
    )

with col2:

    partner_phone = st.text_input(
        "Partner Phone",
        placeholder="Enter phone number",
    )

with col3:

    vehicle = st.selectbox(
        "Vehicle",
        [
            "Bike",
            "Scooter",
            "Cycle",
        ],
    )


if st.button(
    "🛵 Create Delivery Partner"
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
            f"Delivery partner '{partner_name}' created."
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
        <div class="info-card">

            <div class="info-title">
                🛵 Delivery Partner
            </div>

            <div class="info-text">
                <b>Partner:</b> {partner._name}
                &nbsp; | &nbsp;
                <b>Vehicle:</b> {partner.vehicle}
                &nbsp; | &nbsp;
                <b>Status:</b> {availability}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ============================================================
# 7. ACCEPT ORDER
# ============================================================

st.header("7. Accept Order")


if st.button(
    "✅ Accept Order"
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
            "Delivery partner is already busy."
        )

    else:

        st.session_state.delivery_partner.accept_order(
            st.session_state.order
        )

        st.success(
            "Order accepted by delivery partner."
        )


st.divider()


# ============================================================
# 8. OTP & DELIVERY
# ============================================================

st.header("8. Enter OTP & Complete Delivery")

otp = st.number_input(
    "Enter 4-digit OTP",
    min_value=1000,
    max_value=9999,
    step=1,
)


if st.button(
    "🚚 Complete Delivery",
    type="primary",
):

    if st.session_state.order is None:

        st.warning(
            "No order available."
        )

    elif st.session_state.delivery_partner is None:

        st.warning(
            "Create a delivery partner first."
        )

    elif st.session_state.order._status != "Accepted":

        st.warning(
            "The order must be accepted before delivery."
        )

    else:

        order = st.session_state.order
        partner = st.session_state.delivery_partner

        # Verify OTP before calling deliver()
        if order.verify_otp(int(otp)):

            partner.deliver(
                order,
                int(otp),
            )

            st.success(
                f"🎉 Order #{order._order_id} "
                "delivered successfully!"
            )

            st.balloons()

        else:

            st.error(
                "❌ Invalid OTP. Delivery not completed."
            )


st.divider()


# ============================================================
# 9. FINAL SUMMARY
# ============================================================

st.header("9. Delivery Summary")


if st.session_state.order:

    order = st.session_state.order

    st.markdown(
        f"""
        <div class="info-card">

            <div class="info-title">
                🧾 Order Summary
            </div>

            <div class="info-text">

                <b>Order ID:</b>
                #{order._order_id}

                &nbsp; | &nbsp;

                <b>Status:</b>
                {order._status}

                <br><br>

                <b>Total Bill:</b>
                ₹{order.calculate_bill():.2f}

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    if st.session_state.delivery_partner:

        partner = st.session_state.delivery_partner

        st.markdown(
            f"""
            <div class="info-card">

                <div class="info-title">
                    🛵 Delivery Information
                </div>

                <div class="info-text">

                    <b>Delivery Partner:</b>
                    {partner._name}

                    &nbsp; | &nbsp;

                    <b>Vehicle:</b>
                    {partner.vehicle}

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

else:

    st.info(
        "Complete the order flow to see the final summary."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🍔 Food Delivery OOP Project
        &nbsp; • &nbsp;
        Built with Python + Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
