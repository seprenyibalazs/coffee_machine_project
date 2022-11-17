coffees = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 250,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 350,
    },
    'capuchino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 400,
    },

}
profit = 0
resources = {
    'water': 500,
    'milk': 300,
    'coffee': 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated form coins inserted"""
    print("Please insert coints.")
    total = int(input("How many 10 Ft? ")) * 10
    total += int(input("How many 20 Ft? ")) * 20
    total += int(input("How many 50 Ft? ")) * 50
    total += int(input("How many 100 Ft? ")) * 100
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is {change}Ft in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refound.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(F"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("What would you like to drink? espresso/latte/capuchino ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: {profit}Ft")
    else:
        drink = coffees[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
