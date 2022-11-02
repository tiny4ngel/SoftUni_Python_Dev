from project.product import Product


class Drink(Product):
    DRINKS_QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, self.DRINKS_QUANTITY)

