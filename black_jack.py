logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
def deal(cards):
    x=random.choice(cards)
    return x
x=input("Do you want to play a game of Blackjack? Type 'y' or 'n':-").lower()
if(x=='y'):
    print(logo)

    user_cards=[deal(cards),deal(cards)]
    comp_cards=[deal(cards),deal(cards)]

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

    a=input("Type 'y' to get another card, type 'n' to pass:")

