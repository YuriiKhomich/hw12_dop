class Category:
    def __init__(self, name=""):
        self.name = name
        self.items = []

    def __str__(self):
        return self.name


class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.category.items.append(self)

    def __str__(self):
        return self.name


class Client:
    def __init__(self):
        self.items = []

    def clear(self):
        self.items.clear()

    def add_item(self, item):
        self.items.append(ClientAdapter(item))

    def show_items(self):
        pass


class ClientAdapter:
    def __init__(self, item):
        self.item = item
        self.count = int(input("Введіть кількість придбаного товару:"))

    def show(self):
        print(f"""Придбаний товар - {self.item}
Кількість товару, що придбали - {self.count}""")
