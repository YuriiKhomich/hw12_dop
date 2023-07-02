from model import Category, Item
from presenter import get_item_number, choose_category


categories = [Category("Без категорії")]


def admin_menu():
    while True:
        choice = input("""1. Створити категорію
2. Переглянути категорії
3. Створити товар
4. Переглянути товари
5. Показати одну категорію
6. Вийти:""")
        if choice == "1":
            category = Category(input("Назва категорії:"))
            categories.append(category)
            print("Додано")

        if choice == "2":
            for number, category in enumerate(categories, 1):
                print(number, category)

        if choice == "3":
            category_number = choose_category(categories)
            if category_number is None:
                category_number = 0
            category = categories[category_number]
            item = Item(name=input("Назва товару:"), price=input("Ціна товару:"), category=category)

        if choice == "4":
            for number, item in enumerate((item for category in categories for item in category.items), 1):
                print(number, item)

        if choice == "5":
            category_number = choose_category(categories)
            if category_number is not None:
                category = categories[category_number]
                print("Товари категорії")
                for number, item in enumerate(category.items, 1):
                    print(number, item)
                    print("-" * 20)

        if choice == "6":
            break


def client_menu(client):
    while True:
        choice = input("1. Додати товар\n2. Переглянути додані товари\n3. Вийти:")
        if choice == "1":
            items = list(item for category in categories for item in category.items)
            item_number = get_item_number(items)
            if item_number is not None:
                item = items[item_number]
                client.add_item(item)

        if choice == "2":
            for item in client.items:
                item.show()

        if choice == "3":
            break