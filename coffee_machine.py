from recepies import coffees

coffee = 100
milk = 200
water = 300
cost = 0

actual_money = 0


def format_data(type):
    type_name = type['name']
    type_water = type['water_need']
    type_coffee = type['coffee_need']
    type_milk = type['coffee_need']
    type_cost = type['cost_need']
    return f"{type_name}, {type_water}, {type_coffee} {type_milk} {type_cost}"


print(f"Amit választottál{format_data(machine_ask)}")


def machine(machine_ask):
    if machine_ask == "espresso":
        coffee_cost = coffee - 1


machine_ask = input("What would you like to drink? espresso/latte/capuchino")
if machine_ask == "report":
    print(
        f"Coffee: {coffee}\nMilk: {milk}\nWater: {water}\nMoney: {cost}Ft")

pay_10 = int(input("Hány darab 10Ft-ossal fizetsz? "))
actual_money += (pay_10 * 10)


pay_20 = int(input("Hány darab 20Ft-ossal fizetsz? "))
actual_money += (pay_20 * 20)

pay_50 = int(input("Hány darab 50Ft-ossal fizetsz? "))
actual_money += (pay_50 * 50)

pay_100 = int(input("Hány darab 100Ft-ossal fizetsz? "))
actual_money += (pay_100 * 100)
print(actual_money)
