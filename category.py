class Category:

    def _init_(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
    
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description