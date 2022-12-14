import random
class Action_Card:
    def __init__(self, name, cost, add_cards=0, add_actions=0, discard_cards=0, buy_power=0, v_points=0 ,qty=10):
        self.name = name
        self.add_cards = add_cards
        self.add_actions = add_actions
        self.cost = cost
        self.discard_cards = discard_cards
        self.v_points = v_points
        self.buy_power = buy_power
        self.qty = qty

    def add_card(self,player,cards_to_hand):
        for i in range(1,cards_to_hand):
            player.hand.append(player.deck[0])
            player.deck.pop(0)

smithy = Action_Card('smithy',3,4)


class Coin_and_VP_card:
    def __init__(self, name,value,cost,qty=10):
        self.name = name
        self.value = value
        self.cost = cost
        self.qty = qty

copper = Coin_and_VP_card('copper',1,0,55)
silver = Coin_and_VP_card('silver',2,3,25)
gold = Coin_and_VP_card('gold',3,6,25)
estate = Coin_and_VP_card('estate',1,1)
duchy = Coin_and_VP_card('duchy',3,5)
province = Coin_and_VP_card('province',6,8,1)

class Player_deck:
    def __init__(self, name,VP,deck,hand,discard):
        self.name =name
        self.VP = VP
        self.deck = deck
        self.hand = hand
        self.discard = discard

player1 = Player_deck("Aidan",3,[estate,estate,estate,copper,copper,copper,copper,copper,copper,copper],[],[])
player2 = Player_deck("Alex",3,[estate,estate,estate,copper,copper,copper,copper,copper,copper,copper],[],[])

province_counter = 10
buying_options = ["copper","silver","gold","estate","duchy","province","smithy"]

def shuffle(player): #shuffles the players deck
    random.shuffle(player.deck)

shuffle(player1)
shuffle(player2)

def draw_five(player): #puts five cards into the players hand STILL NEED DISCARD SYSTEM
    counter = 0
    while counter < 5:
        #print(player.deck[0].name,counter)
        player.hand.append(player.deck[0])
        player.deck.pop(0)
        counter+=1
    #return(hand)

def get_hand_info(player): # prints the cards in the players hand and returns the value of all the coins in the hand
    coins = 0
    for i in player.hand:
        print(i.name)
        if i.name == "copper" or i.name =="silver" or i.name=="gold":
            coins+=i.value
    print(player.name+" has "+str(coins)+" coins")
    return coins
    
def playing_actions(player):
    pass

def buying_choice(player,coins): 
    print(player.name,"'s Turn")
    print("Buying options are:")
    print(buying_options)
    choice=input("input your choice: ")
    while (string_choice_to_class(choice)).cost > coins or choice!="copper" and choice!="silver" and choice!="gold" and choice!="estate" and choice!="duchy" and choice!="province" and choice!="smithy":
        choice=input("please try again you misspelled something or you dont have enough coins : ")
    player.discard.append(string_choice_to_class(choice))
    decreasing_qty_when_buying(string_choice_to_class(choice))
    print("Your "+player.discard[0].name+" was added to your discard pile")

def hand_to_discard(player):
    player.discard = player.discard + player.hand
    player.hand.clear()

def discard_to_deck(player):
    player.deck = player.discard + player.deck
    player.discard.clear()

def string_choice_to_class(choice_string):
    if choice_string == copper.name:
        return copper
    elif choice_string == silver.name:
        return silver
    elif choice_string == gold.name:
        return gold
    elif choice_string == estate.name:
        return estate
    elif choice_string ==duchy.name:
        return duchy
    elif choice_string == smithy.name:
        return smithy
    else:
        return province

def decreasing_qty_when_buying(card):
    card.qty -=1
    print(card.qty)

def score(player):
    player.deck = player.deck + player.discard + player.hand
    vps = 0
    for i in player.deck:
        print(i.name)
        if i.name == "estate" or i.name =="duchy" or i.name=="province":
            vps+=i.value
    print(player.name+" has "+str(vps)+" VPS")
    return vps

while province.qty > 0:

    draw_five(player1)
    player1_coins=get_hand_info(player1)

    buying_choice(player1,player1_coins)
    hand_to_discard(player1)
    if len(player1.deck)<5:
        discard_to_deck(player1)

print("GAME OVER")
score_player1=score(player1)
score_player2=score(player2)


if score_player1>score_player2:
    print(player1.name," WON SUCK IT",player2.name)
else:
    print(player2.name," WON SUCK IT",player2.name)



#print(player1.deck)
#print(player1.deck[4].name) 
#print(player2.deck[1].value)
#print(estate.value)

#while province_counter > 0:
#buying_choice(player1)





