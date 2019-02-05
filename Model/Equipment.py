class Equipment:

    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

    def __get_name__(self):
        return self.name

    def __get_price__(self):
        return self.price

    def __get_image__(self):
        return self.image

    def __set_name__(self, name):
        self.name = name

    def __set_price(self, price):
        self.price = price

    def __set_image__(self, image):
        self.image =image

