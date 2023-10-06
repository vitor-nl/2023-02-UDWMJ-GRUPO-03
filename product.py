class Product:
    def __init__(self, name, description, date_fabrication, active_or_no, category):
        self.name = name
        self.description = description
        self.date_fabrication = date_fabrication
        self.active_or_no = active_or_no
        self.obj_category = category
    
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_date_fabrication(self):
        return self.date_fabrication
    def get_active_or_no(self):
        return self.active_or_no
    def get_obj_category(self):
        return self.obj_category