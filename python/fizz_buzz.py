print "Welcome to FizzBuzz! :3 "

start = raw_input("Choose anumber between 1 and 100: ")

try:
    if int(start) > 100:
        print "Please enter only numbers between 1 and 100"
    elif int(start) == 0:
        print "Please enter only numbers between 1 and 100"
    else:
        print start

    start = int(start)
    for num in range(1, start+1):

        if num % 3 == 0 and num % 5 == 0:
            print "FizzBuzz"
        elif num % 3 == 0:
            print "Fizz"
        elif num % 5 == 0:
            print "Buzz"
        else:
            print num

except ValueError:
    print "No Fizzbuzzing! Enter a valid number!"

more = raw_input("Would you like to bizzfuzz more? :-) (y/n): ")
if more.lower() in ("y", "yes"):
    print "Yay!"

elif more.lower() in ("n", "no"):
    print "Good Bye, have a fizzbuzzing day!"



