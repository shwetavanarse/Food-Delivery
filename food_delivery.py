# Paste the completed class definitions here.

%%writefile food_delivery.py

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone
        self._wallet_balance = 0

    def add_to_wallet(self, amount):
        if amount >= 0:
            self._wallet_balance += amount

    @abstractmethod
    def notify(self, message):
        pass

    @abstractmethod
    def display_profile(self):
        pass

class Customer(User):
    def __init__(self, name, phone, address):
        super().__init__(name, phone)
        self._address = address
        self.order_history = []
        
    def notify(self, message):
        print(f"Notification for {self._name}: {message}")
        
    def display_profile(self):
        print(f"Name: {self._name}, Phone: {self._phone}, Balance: ₹{self._wallet_balance}, Address: {self._address}")
        
    def place_order(self, restaurant, items):
        order = Order(items)
        self.order_history.append(order)
        return order

class MenuItem:
    def __init__(self, name, price, is_veg):
        self.name = name
        self.price = price
        self.is_veg = is_veg

class Restaurant:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self._menu = []
        
    def add_item(self, menu_item):
        self._menu.append(menu_item)
        
    def get_menu(self):
        return self._menu
        
    def is_open(self):
        return True

class Order:
    _counter = 1
    
    def __init__(self, items):
        self._order_id = f"ORD{Order._counter}"
        Order._counter += 1
        self._items = items
        self._status = "Placed"
        self._otp = 1234
        
    def calculate_bill(self):
        subtotal = sum(item.price for item in self._items)
        gst = subtotal * 0.05
        packaging_fee = 20
        return subtotal + gst + packaging_fee
        
    def estimated_time(self):
        return 30
        
    def update_status(self, new_status):
        self._status = new_status
        
    def verify_otp(self, otp):
        return self._otp == otp

class DeliveryPartner(User):
    def __init__(self, name, phone, vehicle):
        super().__init__(name, phone)
        self.vehicle = vehicle
        self.is_available = True
        self.rating = 0.0

    def notify(self, message):
        print(f"Delivery Partner {self._name} Notification: {message}")

    def display_profile(self):
        print(f"Name: {self._name}, Phone: {self._phone}, Vehicle: {self.vehicle}, Rating: {self.rating}")

    def accept_order(self, order):
        order.update_status("Accepted")
        self.is_available = False
        print(f"{self._name} has accepted the order.")

    def deliver(self, order, otp):
        if order.verify_otp(otp):
            order.update_status("Delivered")
            self.is_available = True
            print(f"OTP verified. Order delivered by {self._name}.")
        else:
            print("Incorrect OTP! Order not delivered.")
