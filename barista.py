import random
from random import choice

## 1. The processOrder function will take in a quantity and item off the item list.
## 2. I am declaring a global variable named total so it can be accessed in other functions later in the program
## 3. If the quantity requested is more that whats avalible a message prints to the user to pick something else
## 4. The quantity gets updated as the items get purchased 
def processOrder(quantity, item_list):
    global total
    if quantity > item_list[2]:
        print("We don't have enough please order somthing else!")
        process()
    else:
        total += item_list[1] * quantity
        item_list[2] -= quantity

total = 0

## The menu of items with the price and quantity avaliable for the day
MENU = ["Coffee", float(3.99), 50], ["Tea", float(2.99), 20], ["Juice", float(4.99), 20], ["Bagel", float(2.99), 30], ["Muffin", float(1.99), 10], ["Croissant", float(3.99), 5], ["Sandwich", float(4.99), 6], ["Cookie", float(1.99), 10], ["Mystery", float(9.99), 1]

## The random item if a user selects the mystery item
RANDOM_ITEM = {"A Pack of Coffee Bean Socks", "Free Coffee for a year", "A high five (see associate to redeem)", "1 Menu item for free", "Buy 1 get 1 half off for a month", "Free Coffee mug with a purchase of 1 Menu Item", "One month gym membership on us"}

## Welcoming the user and prompting them to order when ready
print("Welcome to the coffee bean! Please order when your ready!")

## The menu items listed for the user with prices
def menuItems():  
    print("[1]", MENU[0][0:2],
      "\n[2]", MENU[1][0:2],
      "\n[3]", MENU[2][0:2],
      "\n[4]", MENU[3][0:2],
      "\n[5]", MENU[4][0:2],
      "\n[6]", MENU[5][0:2],
      "\n[7]", MENU[6][0:2],
      "\n[8]", MENU[7][0:2],
      "\n[9]", MENU[8][0:2])

def randomItem():
    print("Congrats you get a random item of: " + random.choice(list(RANDOM_ITEM)))

## Checks the total to see if the user qualifies for a discount. If they qualify they will get 10% off their purchase
def checkTotal():
    if total >= 10.0:
        checkPaymentMethod(total)
        print("For spending over $10, You qualify for 10" + "%" + " off")
        new_total = applyDiscount(total)
        final_total = salesTax(new_total)
        print("Your new total is $" + str(round(final_total, 2)))
        quit()
    elif total < 10.0:
        checkPaymentMethod(total)
        final_total = salesTax(total)
        print("Thank you for ordering!\nYour total cost is: $" +  str(round(final_total, 2)))
        quit()

## Logic for the discount
def applyDiscount(total):
    discount = total * .10
    discounted_total = total - discount
    return discounted_total


def checkPaymentMethod(total):
    while total < 5.0:
        choice = (input("\nWill you be using cash or card?\n")).upper()
        if choice == "CARD":
            creditCardProcess()
            process()    
        elif choice == "CASH":
            break
        else:
            print("??")


def creditCardProcess():
    print("We have a minimue credit card purchase of $5.00, Please add more items")

def salesTax(total):
    tax = total * .07
    tax_total = total + tax
    return tax_total


## The ordering process
def process():
    menuItems()
    while True:
        choice, quantity, = (input("\nWhat will you be ordering today?\n")).upper(), int(input("\nHow many would you like?\n"))

## I eventually want to refactor this to loop through and grab the menu item selected
        if choice == "COFFEE":
            processOrder(quantity, MENU[0])
        elif choice == "TEA":
            processOrder(quantity, MENU[1])
        elif choice == "JUICE":
            processOrder(quantity, MENU[2])
        elif choice == "BAGEL":
            processOrder(quantity, MENU[3])
        elif choice == "MUFFIN":
            processOrder(quantity, MENU[4])
        elif choice == "CROISSANT":
            processOrder(quantity, MENU[5])
        elif choice == "SANDWICH":
            processOrder(quantity, MENU[6])
        elif choice == "COOKIE":
            processOrder(quantity, MENU[7])
        elif choice == "MYSTERY":
            processOrder(quantity, MENU[8])
            randomItem()
        else:
            print("Invalid Item, please choose an item from our menu")
            process()

        more_items = (input("Do you want to order more items?\n")).lower()
        if more_items == "yes" or more_items == "y":
            menuItems()
        else:
            checkTotal()

process()

# Tell them to type in a menu item 
