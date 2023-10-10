class Order:
    
    def __init__(self, total_price, status, client):
        self.total_price = total_price
        self.stauts = status
        self.obj_client = client

    def get_total_price(self):
        return self.total_price

    def get_status(self):
        return self.total_price

    def get_obj_client(self):
        return self.obj_client