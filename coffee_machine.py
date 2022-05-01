MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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


def check_resource(order):
     a=MENU[order]["ingredients"]
     if a['water']<resources['water'] and a['milk']<resources['milk'] and a['coffee']<resources['coffee']:
         return True
     return False

def report(resources):
    print(f"water:{resources['water']}")
    print(f"milk:{resources['milk']}")
    print(f"coffee:{resources['coffee']}")

def money_counter():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:-"))
    dimes = int(input("How many dimes?:-"))
    nickles = int(input("How many nickles?:-"))
    penneies = int(input("How many penneies?:-"))
    money = quarters * quarter + penneies * penney + dimes * dime +nickles * nickle
    change = money-MENU[order]['cost']
    if change>0:
        print(f"Here is ${change} in change")
    else:
        print("Sorry that's not enough money. Money refunded.")


def place_order(order):
    global resources
    global y
    if(check_resource(order)==True):
        money_counter()
        print(f"Here is your {order} enjoy!!!")

        remaining_water = resources['water']-MENU[order]['ingredients']['water']
        remaining_milk = resources['milk']-MENU[order]['ingredients']['milk']
        remaining_coffee = resources['coffee']-MENU[order]['ingredients']['coffee']

        resources["water"] = remaining_water
        resources["milk"] = remaining_milk
        resources["coffee"] = remaining_coffee
    else:
        print("Sorry  not enough resources.")
        y = "no"

quarter = 0.25
penney = 0.01
nickle = 0.05
dime = 0.10
y ="yes"
while(y=="yes"):
    order = input("Whay would you like to have(Espresso,Latte,Cappuccino).:-").lower()
    if (order == "report"):
        report(resources)
    else:
        place_order(order)