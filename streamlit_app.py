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
# SIMPLE CSS
# ============================================================

st.markdown(
    """
    <style>
        /* Main background */
        .stApp {
            background-color: #fffaf7;
        }

        /* Main content width */
        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Headings */
        h1 {
            color: #e85d2a !important;
            font-weight: 800 !important;
        }

        h2 {
            color: #252525 !important;
            font-weight: 750 !important;
        }

        h3 {
            color: #333333 !important;
        }

        /* Buttons */
        .stButton > button {
            border-radius: 10px;
            font-weight: 600;
            min-height: 42px;
        }

        /* Input boxes */
        input {
            border-radius: 8px !important;
        }

        /* Select boxes */
        div[data-baseweb="select"] > div {
            border-radius: 8px !important;
        }

        /* Metrics */
        div[data-testid="stMetric"] {
            background-color: white;
            border: 1px solid #f0ddd5;
            border-radius: 12px;
            padding: 15px;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.04);
        }

        /* Tables */
        div[data-testid="stTable"] {
            background-color: white;
            border-radius: 12px;
            border: 1px solid #f0ddd5;
            overflow: hidden;
        }

        /* Alerts */
        div[data-testid="stAlert"] {
            border-radius: 10px;
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

st.title("🍔 Food Delivery System")

st.caption(
    "Simple and interactive Streamlit interface "
    "for the OOP Food Delivery project"
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
        placeholder="Enter customer name"
    )

with col2:
    customer_phone = st.text_input(
        "Phone",
        placeholder="Enter phone number"
    )

with col3:
    customer_address = st.text_input(
        "Address",
        placeholder="Enter delivery address"
    )


if st.button(
    "👤 Create Customer",
    type="primary"
):

    if (
        customer_name
        and customer_phone
        and customer_address
    ):

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

    st.info(
        f"👤 Customer: {customer._name}   |   "
        f"💰 Wallet: ₹{customer._wallet_balance:.2f}"
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
    format="%.2f"
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
        f"₹{st.session_state.customer._wallet_balance:.2f}"
    )


st.divider()


# ============================================================
# 3. RESTAURANT MENU
# ============================================================

st.header("3. Restaurant Menu")

st.write(
    f"🍽️ **{restaurant.name}** — "
    f"📍 {restaurant.location}"
)


menu_data = []

for item in restaurant.get_menu():

    menu_data.append(
        {
            "Item": item.name,
            "Price": f"₹{item.price:.2f}",
            "Type": (
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
    placeholder="Choose food items..."
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

    st.info(
        f"Subtotal: ₹{subtotal:.2f}  |  "
        f"GST (5%): ₹{gst:.2f}  |  "
        f"Packaging: ₹{packaging:.2f}  |  "
        f"**Total: ₹{total:.2f}**"
    )


if st.button(
    "🛒 Place Order",
    type="primary"
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
            order._order_id
        )

    with c2:

        st.metric(
            "Status",
            order._status
        )

    with c3:

        st.metric(
            "Estimated Time",
            f"{order.estimated_time()} min"
        )

    st.write(
        f"💳 **Bill:** ₹{order.calculate_bill():.2f}"
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
        placeholder="Enter partner name"
    )

with col2:

    partner_phone = st.text_input(
        "Partner Phone",
        placeholder="Enter phone number"
    )

with col3:

    vehicle = st.selectbox(
        "Vehicle",
        [
            "Bike",
            "Scooter",
            "Cycle"
        ]
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

    st.info(
        f"🛵 Partner: {partner._name}   |   "
        f"🚗 Vehicle: {partner.vehicle}   |   "
        f"Status: {availability}"
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
# 8. OTP AND DELIVERY
# ============================================================

st.header("8. Enter OTP & Complete Delivery")

otp = st.number_input(
    "Enter 4-digit OTP",
    min_value=1000,
    max_value=9999,
    step=1
)


if st.button(
    "🚚 Complete Delivery",
    type="primary"
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

        # Check OTP first.
        if order.verify_otp(int(otp)):

            partner.deliver(
                order,
                int(otp)
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
# 9. DELIVERY SUMMARY
# ============================================================

st.header("9. Delivery Summary")


if st.session_state.order:

    order = st.session_state.order

    st.write(
        f"**Order ID:** #{order._order_id}"
    )

    st.write(
        f"**Status:** {order._status}"
    )

    st.write(
        f"**Total Bill:** "
        f"₹{order.calculate_bill():.2f}"
    )

    if st.session_state.delivery_partner:

        partner = st.session_state.delivery_partner

        st.write(
            f"**Delivery Partner:** {partner._name}"
        )

        st.write(
            f"**Vehicle:** {partner.vehicle}"
        )

else:

    st.info(
        "Complete the order flow to see "
        "the final summary."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🍔 Food Delivery OOP Project • "
    "Built with Python + Streamlit"
)
