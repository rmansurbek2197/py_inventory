class Product:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty


class Inventory:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def sell(self, name, qty):
        for p in self.products:
            if p.name == name and p.qty >= qty:
                p.qty -= qty

    def low_stock(self):
        return [p.name for p in self.products if p.qty < 5]
