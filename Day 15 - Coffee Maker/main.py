MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print('Here is the current report for the coffee machine:')
    for key, value in resources.items():
        print(key, ' ', value)


user_choice = ''
while user_choice != 'Off':
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')

    if user_choice == 'report':
        print_report()
