
def choose_category(categories):
    for number, category in enumerate(categories, 1):
        print(number, category)
    number = input("Оберіть номер категорії:")
    if number.isdigit() and 0 < int(number) <= len(categories):
        return int(number) - 1


def get_item_number(items):
    items = list(items)
    for number, item in enumerate(items, 1):
        print(number, item)
    number = input("Введіть номер товару:")
    if number.isdigit() and 0 < int(number) <= len(items):
        return int(number) - 1
