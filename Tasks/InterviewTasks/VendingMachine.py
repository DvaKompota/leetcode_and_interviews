# Problem Statement
# You need to design a Vending Machine which
# Accepts coins of 1,5,10,25 Cents i.e. penny, nickel, dime, and quarter.
# Allow user to select products Coke(25), Pepsi(35), Soda(45)
# Allow user to take refund by canceling the request.
# Return selected product and remaining change if any.
# While a UI would be awesome, the expectation is that this is a program
# run on the command-line, which will accept input via keyboard.
# Choose what language you want, extra credit for Python 3.
#
# Expected results:
# > python3 VendingMachine.py
# Vending Machine> What would you like to drink?
# Keyboard Entry> Coke,1Q
# Vending Machine> Here you go, enjoy!
#
# Vending Machine> What would you like to drink?
# Keyboard Entry> Coke,1D
# Vending Machine> Sorry, you need more money for that.
#
# Vending Machine> What would you like to drink?
# Keyboard Entry> Coke,3D
# Vending Machine> Here you go, enjoy! Your change is 1N
#
# Q=quarter, D=dime, N=nickel, P=penny
import re


products = {"Coke": 25, "Pepsi": 35, "Soda": 45}
coins = {"P": 1, "N": 5, "D": 10, "Q": 25, }


def input_converter(order_received: str):
    coma_count = re.findall("\\,", order_received)
    if len(coma_count) < 1:
        print("Please divide the product name and the coins with a coma")
        return None, None
    elif len(coma_count) > 1:
        print("Please use only one coma — to divide the product name from the coins")
        return None, None
    order_no_spaces = order_received.replace(" ", "")
    order_split = order_no_spaces.split(",")
    product = order_split[0]
    if product not in products:
        print("No such product available")
        return None, None
    else:
        coin_quantity = re.findall("\\d", order_split[1])
        coin_type = re.findall("\\D", order_split[1])
        if len(coin_quantity) != len(coin_type):
            print("Invalid combination of coins: each coin type should have its quantity and vice versa")
        else:
            amount = 0
            for i in range(len(coin_type)):
                if coin_type[i] not in coins:
                    amount = None
                    print("Invalid type of coin — please insert only valid coins: "
                          "(Q)uarter, (D)ime, (N)ickel, (P)penny")
                else:
                    amount += coins[coin_type[i]] * int(coin_quantity[i])
            return product, amount


def amount_to_coins_converter(amount):
    amount_in_cents = amount
    amount_in_coins = ""
    for coin in ["Q", "D", "N", "P"]:
        if amount_in_cents >= coins[coin]:
            coins_quantity = int(amount_in_cents/coins[coin])
            amount_in_coins += f"{coins_quantity}{coin}"
            amount_in_cents -= coins_quantity * coins[coin]
    return amount_in_coins


def take_order():
    while True:
        drink, money = input_converter(input("What would you like to drink [Coke, Pepsi, Soda]? "))
        if drink is not None and money is not None:
            break
    price = products[drink]
    if money < price:
        print(f"Sorry, you need more money for that. {drink}'s price is {price} cents")
    elif money == price:
        print("Here you go, enjoy!")
    else:
        change = amount_to_coins_converter(money - price)
        print(f"Here you go, enjoy! Your change is {change}")


if __name__ == '__main__':
    take_order()
