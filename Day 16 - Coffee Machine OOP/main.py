from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffeemaker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()


running = True
while running:
    customer_choice = input(f"What would you like? ({my_menu.get_items()}): ")

    if customer_choice == "off":
        running = False
    elif customer_choice == "report":
        my_coffeemaker.report()
        my_money_machine.report()
    else:
        menu_item = my_menu.find_drink(customer_choice)

        if my_coffeemaker.is_resource_sufficient(menu_item):
            if my_money_machine.make_payment(menu_item.cost):
                my_coffeemaker.make_coffee(menu_item)
