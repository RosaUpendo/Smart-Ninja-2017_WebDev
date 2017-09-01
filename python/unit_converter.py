
print "Greetings, human user! I can help you by converting kilometers into miles..."

while True:
    print "Tell me your kilometers and I'll tell you your miles!"

    try:
        km = raw_input("Kilometers: ")
        km = float(km)
        miles = km * 0.621371

        print km, "km are ", miles, "miles"

    except ValueError as e:
        print "Error! Please give me numbers only, I hate to eat letters."
        break

    more = raw_input("Yum Yum Yum, numbers! Would you like to convert more? :-) (y/n): ")
    if more.lower() in ("y", "yes"):
        print "Yum, more numbers coming!"

    elif more.lower() in ("n", "no"):
        print "So be it. It was a pleasure converting for you, human user!"
        break




