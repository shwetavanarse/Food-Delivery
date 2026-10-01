import streamlit as st
from food_delivery import Customer, DeliveryPartner, MenuItem, Restaurant

st.set_page_config(page_title="Food Delivery App", page_icon="🍔")
st.title("🍔 OOP Food Delivery App")
st.caption("Simple Streamlit interface for the Food Delivery OOP project")

if "customer" not in st.session_state:
    st.session_state.customer = None
if "restaurant" not in st.session_state:
    r = Restaurant("Food Hub", "Sambhajinagar")
    r.add_item(MenuItem("Veg Burger", 120, True))
    r.add_item(MenuItem("Pizza", 250, True))
    r.add_item(MenuItem("French Fries", 100, True))
    r.add_item(MenuItem("Cold Drink", 60, True))
    st.session_state.restaurant = r
if "order" not in st.session_state:
    st.session_state.order = None
if "delivery_partner" not in st.session_state:
    st.session_state.delivery_partner = None

st.header("1️⃣ Create Customer")
with st.form("customer_form"):
    name = st.text_input("Customer Name")
    phone = st.text_input("Phone Number")
    address = st.text_input("Delivery Address")
    if st.form_submit_button("Create Customer"):
        if name and phone and address:
            st.session_state.customer = Customer(name, phone, address)
            st.success(f"Customer '{name}' created successfully!")
        else:
            st.warning("Please fill in all customer details.")

st.header("2️⃣ Add Wallet Balance")
if st.session_state.customer:
    amount = st.number_input("Amount to Add (₹)", min_value=0.0, step=50.0)
    if st.button("Add Balance"):
        st.session_state.customer.add_to_wallet(amount)
        st.success(f"₹{amount:.2f} added to wallet.")
else:
    st.warning("Create a customer first.")

st.header("3️⃣ Restaurant Menu")
restaurant = st.session_state.restaurant
for item in restaurant.get_menu():
    veg = "🟢 Veg" if item.is_veg else "🔴 Non-Veg"
    st.write(f"**{item.name}** — ₹{item.price:.2f} | {veg}")

st.header("4️⃣ Place Order")
if st.session_state.customer:
    menu = restaurant.get_menu()
    selected = st.multiselect("Select food items", [x.name for x in menu])
    if st.button("Place Order"):
        if selected:
            items = [x for x in menu if x.name in selected]
            st.session_state.order = st.session_state.customer.place_order(restaurant, items)
            order = st.session_state.order
            st.success(f"Order {order._order_id} placed successfully!")
            st.write(f"**Bill:** ₹{order.calculate_bill():.2f}")
            st.write(f"**Estimated Time:** {order.estimated_time()} minutes")
        else:
            st.warning("Select at least one item.")
else:
    st.warning("Create a customer first.")

st.header("5️⃣ Create Delivery Partner")
with st.form("delivery_form"):
    dp_name = st.text_input("Delivery Partner Name")
    dp_phone = st.text_input("Delivery Partner Phone")
    vehicle = st.selectbox("Vehicle", ["Bike", "Scooter", "Car"])
    if st.form_submit_button("Create Delivery Partner"):
        if dp_name and dp_phone:
            st.session_state.delivery_partner = DeliveryPartner(dp_name, dp_phone, vehicle)
            st.success(f"Delivery partner '{dp_name}' created!")
        else:
            st.warning("Please fill in all delivery partner details.")

st.header("6️⃣ Accept Order")
if st.session_state.order and st.session_state.delivery_partner:
    if st.button("Accept Order"):
        st.session_state.delivery_partner.accept_order(st.session_state.order)
        st.success("Order accepted!")
else:
    st.warning("Create an order and delivery partner first.")

st.header("7️⃣ Enter OTP")
if st.session_state.order:
    st.info("Demo OTP: 1234")
    otp = st.number_input("Enter OTP", min_value=0, max_value=9999, step=1)
    if st.button("Verify OTP"):
        if st.session_state.order.verify_otp(otp):
            st.success("OTP is correct!")
        else:
            st.error("Incorrect OTP.")

st.header("8️⃣ Complete Delivery")
if st.session_state.order and st.session_state.delivery_partner:
    delivery_otp = st.number_input("OTP to complete delivery", min_value=0, max_value=9999, step=1, key="delivery_otp")
    if st.button("Complete Delivery"):
        st.session_state.delivery_partner.deliver(st.session_state.order, delivery_otp)
        if st.session_state.order.verify_otp(delivery_otp):
            st.success("🎉 Delivery completed successfully!")
        else:
            st.error("Delivery failed. Incorrect OTP.")
else:
    st.warning("Create an order and delivery partner first.")

st.header("📦 Current Order Status")
if st.session_state.order:
    st.write(f"**Order ID:** {st.session_state.order._order_id}")
    st.write(f"**Status:** {st.session_state.order._status}")
else:
    st.write("No order placed yet.")
