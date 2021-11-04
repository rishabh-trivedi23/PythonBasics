# TODO 1 : print report
# TODO 2 : Check resource sufficient
# TODO 3 : Process coins
# TODO 4 : check transaction successful
# TODO 5 : Make Coffee

from coffee_data import MENU, resources

working = True

current_resources = resources
balance = 0

def coffee(option):
        water_req= MENU[option]['ingredients']['water']
        coffee_req = MENU[option]['ingredients']['coffee']
        available_water = current_resources['water']
        available_milk = current_resources['milk']
        available_coffee = current_resources['coffee']
        price = MENU[option]['cost']
        if option == "espresso":
            if water_req > available_water and coffee_req > available_coffee:
                print("not enough resources")
            else:
                payment_check, price = payment(price)
                print(f"Here is ${payment_check} in change.")
                print(f"Here is your {option} ☕. Enjoy!")
                remaining_water = available_water - water_req
                remaining_coffee = available_coffee - coffee_req
                return remaining_water, remaining_coffee, price
        else:
            milk_req = MENU[option]['ingredients']['milk']
            if water_req > available_water and coffee_req > available_coffee and milk_req > available_milk:
                print("not enough resources")
            else:
                payment_check, price = payment(price)
                print(f"Here is ${payment_check} in change.")
                print(f"Here is your {option} ☕. Enjoy!")
                remaining_water = available_water - water_req
                remaining_milk = available_milk - milk_req
                remaining_coffee = available_coffee - coffee_req
                return remaining_water, remaining_coffee, remaining_milk, price

def report(current_resources):
    print(f"Water: {current_resources['water']}ml")
    print(f"Water: {current_resources['milk']}ml")
    print(f"Water: {current_resources['coffee']}g")
    print(f"Money in the bank: ${balance}")

def payment(price):
    print("Please insert coins")
    user_quarters = int(input("how many quarters?: "))
    user_dimes = int(input("how many dimes?: "))
    user_nickles = int(input("how many nickles?: "))
    user_pennies = int(input("how many pennies?: "))
    total_count = (user_quarters * 0.25) + (user_dimes * 0.10) + (user_nickles * 0.05) + (user_pennies * 0.01)
    if total_count >= price:
        change = round((total_count - price),2)
        return change, price
    else:
        print("Sorry that's not enough money. Money refunded.")


while working:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report(current_resources)
    elif user_input == "off":
        working = False
    elif user_input == "espresso":
        updated_water, updated_coffee, price = coffee(user_input)
        current_resources['water'] = updated_water
        current_resources['coffee'] = updated_coffee
        balance= balance + price
    elif user_input == "latte" or user_input == "cappuccino":
        updated_water, updated_coffee, updated_milk, price = coffee(user_input)
        current_resources['water'] = updated_water
        current_resources['coffee'] = updated_coffee
        current_resources['milk'] = updated_milk
        balance= balance + price
    else:
        print("please select correct option!")
