class Bicycle:
    def __init__(self, brand, frame_size, age, service):
        self.brand = brand
        self.frame_size = frame_size
        self.age = age
        self.service = service

    def add_years(self, new_age):
            self.age += new_age

    def update_service(self, new_date):
            self.service = new_date

def list_bicycles(bicycles):
    if not bicycles:
        print "Looks like you don't have any bicycles in your program right now."
    else:
        for index, bicycle in enumerate(bicycles):
            print "%s) %s %s with %s years so far. Last service: %s" % (index+1, bicycle.brand, bicycle.frame_size,
                bicycle.age, bicycle.service)

def create_bicycle(brand, frame_size, years_alive, service_done, bicycles):

    try:
        years_alive = years_alive.replace(",", ".")
        age = float(years_alive)

        new = Bicycle(brand=brand, frame_size=frame_size, age=age, service=service_done)

        bicycles.append(new)

        return True
    except ValueError:
        return False

def add_new_bike(bicycles):
   brand = raw_input("Please enter bicycle brand: ")
   frame_size = raw_input("Please enter the frame size: ")
   years_alive = raw_input("Please enter years of usage: ")
   service_done = raw_input("Please enter general service date of the bicycle (DD.MM.YYYY): ")

   new_bike = create_bicycle(brand, frame_size, years_alive, service_done, bicycles)

   if new_bike:
       print "You added a new bicycle to your program: %s %s!" % (brand,frame_size)
   else:
       print "Please enter a valid number of years."

def select_bike(bicycles):
    print "Which bicycle would you like to edit (enter ID-number)? "
    print ""
    list_bicycles(bicycles)
    print ""

    selected_bike = raw_input("ID number of the bicycle: ")
    return bicycles[int(selected_bike) - 1]

def add_more_years(bicycles):
    selected = select_bike(bicycles)
    print "You have selected this bicycle: %s %s , with updated years of: %s usage." % (selected.brand, selected.frame_size, selected.age)
    print ""
    added_years = raw_input("Enter how many years you would like to add to the bicycle: ")

    try:
        added_years = added_years.replace("," , ".")
        new_age =float(added_years)

        selected.add_years(new_age)
        print "The years of the bicycle %s %s have been updated to: %s." % (selected.brand, selected.frame_size, selected.age)
    except ValueError:
        print "Please enter just one number."

def edit_service(bicycles):
    selected = select_bike(bicycles)
    print "You have selected this bicycle: %s %s , the new service date: %s ." % (selected.brand, selected.frame_size, selected.service)
    new_service = raw_input("Enter a new general service date (DD.MM.YYYY): ")
    selected.update_service(new_date=new_service)
    print "The service date was updated."

def save_txt(bicycles):
    with open("bicycles.txt", "w+") as bike_f:
        for bicycle in bicycles:
            bike_f.write("%s, %s, %s, %s\n" % (bicycle.brand, bicycle.frame_size, bicycle.age, bicycle.service))

def main():
    print "Welcome to your bicycle manager!"

    bicycles = []

    with open("bicycles.txt", "r") as bike_f:
        for line in bike_f:
            try:
                brand, frame_size, age, service = line.split(",")
                create_bicycle(brand, frame_size, age, service, bicycles)
            except ValueError:
                continue
    while True:
        print "Please enter one of the following: "
        print "a: Show list of all bicycle"
        print "b: Add new bicycle"
        print "c: Edit years of usage for one bicycle"
        print "d: Edit service date for one bicycle"
        print "e: Quit program and go outside to drive a bike!"

        answere = raw_input("What would you like to do (a/b/c/d/e)?")

        if answere.lower() == "a":
            list_bicycles(bicycles)
        elif answere.lower() == "b":
            add_new_bike(bicycles)
        elif answere.lower() == "c":
            add_more_years(bicycles)
        elif answere.lower() == "d":
            edit_service(bicycles)
        elif answere.lower() == "e":
            print "Enjoy your riiiiide, good bye!"
            save_txt(bicycles)
            break
        else:
            print "This was not a valid input. Please type only one of the following letters: a, b, c, d, e"
            print "a: Show list of all bicycle"
            print "b: Add new bicycle"
            print "c: Edit years of usage for one bicycle"
            print "d: Edit service date for one bicycle"
            print "e: Cancel"


if __name__ == "__main__":
    main()
