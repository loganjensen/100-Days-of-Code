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
    "money": 0
}


def print_report():
    """
    Prints the remaining amount for each ingredient in the coffee machine
    """
    print('Here is the current report for the coffee machine:')
    for key, value in resources.items():
        if key == 'water':
            print(f'{value} mL of water')
        elif key == 'milk':
            print(f'{value} mL of milk')
        elif key == 'coffee':
            print(f'{value} g of coffee')
        elif key == 'money':
            print(f'${value:.2f} of money')


def check_resources(selection):
    """
    Check's the coffee maker's resources to ensure enough of each ingredient exists.
    Returns True if it has all the ingredients, and False otherwise
    """
    drink_chosen = MENU[selection]

    # Ensure there are enough ingredients to make the coffee selection
    for ingredient, amount_needed in drink_chosen['ingredients'].items():
        curr_resource_value = resources.get(ingredient)
        if amount_needed > curr_resource_value:
            print(f'Error. Not enough {ingredient} remaining. Make another selection.')
            return False

    return True


def subtract_resources(selection):
    """
    Subtracts the amount needed to make a coffee drink from the coffee machine's resources
    Does not return any value
    """
    drink_chosen = MENU[selection]

    for ingredient, amount_needed in drink_chosen['ingredients'].items():
        resources[ingredient] -= amount_needed


def process_change():
    quarters = input('How many quarters are you inserting? ')
    dimes = input('How many dimes are you inserting? ')
    nickels = input('How many nickels are you inserting? ')
    pennies = input('How many pennies are you inserting? ')

    change_total = (0.25 * int(quarters)) + (0.1 * int(dimes)) + (0.5 * int(nickels)) + (0.1 * int(pennies))

    return change_total


"""
Below is the implementation of the coffee machine software.
"""
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
        # Ensure coffee machine has enough resources to make drink
        has_resources = check_resources(user_choice)

        if has_resources:
            subtract_resources(user_choice)
            total_user_change = process_change()

            # Verify customer inserted enough money
            if total_user_change < MENU[user_choice]['cost']:
                print('Sorry, that\'s not enough money. Money refunded.')
                break
            else:
                coffee_cost = MENU[user_choice]['cost']
                resources['money'] += coffee_cost
                change_needed = total_user_change - coffee_cost
                print('Here is your latte! Enjoy! ??????')
                print(f'Here is ${change_needed:.2f} in change.')


print('Thanks for using the coffee maker program!')