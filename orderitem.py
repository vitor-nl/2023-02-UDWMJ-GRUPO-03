class OrderItem:
    
    def __init__(self, quantity, unitary_price, order, product):
        self.quantity = quantity
        self.unitary_price = unitary_price
        self.obj_order = order
        self.obj_product = product
        
    def get_quantity(self):
        return self.quantity

    def get_unitary_price(self):
        return self.unitary_price

    def get_obj_order(self):
        return self.obj_order

    def get_obj_product(self):
        return self.obj_product