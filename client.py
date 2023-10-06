class Client:
    
    def __init__(self, first_name, last_name, address, cell_phone, email, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.cell_phone = cell_phone
        self.email = email
        self.gender = gender
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_address(self):
        return self.address
    
    def get_cell_phone(self):
        return self.cell_phone
    
    def get_email(self):
        return self.email
    
    def get_gender(self):
        return self.gender