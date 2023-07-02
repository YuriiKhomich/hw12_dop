from view import admin_menu, client_menu
from model import Client

while True:
    choice = input("1. Адміністратор\n2. Клієнт\n3. Вийти")
    if choice == "1":
        admin_menu()
    if choice == "2":
        client_menu(Client())
    if choice == "3":
        break
