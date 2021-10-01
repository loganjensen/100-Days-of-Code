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
        if key == 'water' or key == 'milk':
            print(f'{value} mL')
        elif key == 'coffee':
            print(f'{value} g')

def check_resources(selection):
    drink_chosen = MENU[selection]

    for ingredient, amount_needed in drink_chosen['ingredients'].items():
        curr_resource_value = get(resources[ingredient])
        if amount_needed > curr_resource_value:
            print(f'Error. Not enough {ingredient} remaining. Make another selection.')

user_choice = ''
while user_choice != 'Off':
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')

    # Verify user chose correct option; re-prompt user if not
    if user_choice not in ('espresso', 'latte', 'cappuccino', 'Report', 'Off'):
        print('Invalid choice. Please choose espresso, latte, or cappuccino.')
        print('You can also exit by choosing \'Off\'')
    elif user_choice == 'Report':
        print_report()
    elif user_choice == 'Off':
        break
    else:
        check_resources(user_choice)

print('Thanks for using the coffee maker program!')