import time

print("Hello! I am Pipí, the Breakfast Bot.")
time.sleep(2)
print("Today we have two breakfasts available.")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(2)
while True:
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n\n").lower()
        if "waffles" in response:
            print("Waffles it is.")
            time.sleep(2)
            break
        elif "pancakes" in response:
            print("Pancakes it is.")
            time.sleep(2)
            break
        else:
            print("Sorry, that's not on our menu.")
            time.sleep(2)
    print("Your order will be ready shortly")
    time.sleep(2)
    while True:
        another = input("Would you like to place another order? "
                        "Please say 'yes' or 'no'.\n").lower()
        if "yes" in another:
            print("Very good, I'm happy to take another order.")
            time.sleep(2)
            break
        elif "no" in another:
            print("Ok, goodbye!")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    if "no" in another:
        break
