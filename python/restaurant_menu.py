print "Welcome to your menu program! <3"

menu = {}

while True:
    daily_dish = raw_input("Enter a daily dish here: ")
    price = raw_input("price for daily dish '%s': " % daily_dish)
    menu[daily_dish] = price
    print "You added a new daily dish: ", daily_dish, ", the price is ", price, "Euros."

    new = raw_input("Would you like to enter a new dish? (yes/no)")

    if new.lower() == "no":
        break

print "On the menu today: %s" % menu

with open("daily_menu.txt", "w+") as menu_file:
    menu_file.write("Our daily menu is cooked with organic ingredients and love <3\n")
    for dish in menu:
        menu_file.write("%s, %s EUR\n" % (dish, menu[dish]))

print "Have a yummy day!"




