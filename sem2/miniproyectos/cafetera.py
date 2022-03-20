def print_report():
    print(f"The machine have water: {water}ml, milk {milk}ml, sugar {sugar}g and coffe {coffe}g. ")


def fill_machine():
    global water, milk, sugar, coffe

    water_ml = int(input("How much water do you want to add?"))
    milk_ml = int(input("How much milk do you want to add?"))
    sugar_g = int(input("How much sugar do you want to add?"))
    coffe_g = int(input("How much coffe do you want to add?"))

    water += water_ml
    milk += milk_ml
    sugar += sugar_g
    coffe += coffe_g

def enough_recourses(drinks_name):
    if drinks_name == "caffelatte":
        return water >= 150 and milk >= 50 and sugar >= 15 and coffe >= 5
    elif drinks_name == "espresso":
        return water >= 200 and  coffe >= 10
    elif drinks_name == "macchiatto":
        return water >= 150 and milk >= 80 and sugar >= 20 and coffe >= 8


def make_coffe(drinks_name):
    global water, milk, sugar, coffe

    if enough_recourses(drinks_name):
        if drinks_name == "caffelatte":
            water -= 150
            milk -= 50
            sugar -= 15
            coffe -= 5
             
        elif drinks_name == "espresso":
            water -= 200
            coffe -= 10
        elif drinks_name == "macchiatto":
            water -=150
            milk -= 80
            sugar -= 20
            coffe -= 8

        print(f"Here is your {drinks_name}, enjoy! ")            

    else:
        print("There isn't enough recources to make you coffe,sorry!")    

coffe_machine_on = True

water = 500
milk = 300
sugar = 100
coffe = 40

drinks = ["caffelatte","espresso","macchiatto"]

while coffe_machine_on:
    option = input("What would you like to have? (caffelatte, espresso, macchiatto), type e, for exit\n")

    if option == "e":
        print("Thank you, come again!\n")
        coffe_machine_on = False
    elif option in drinks:
        #pass # Make a drink
        make_coffe(option)
    elif option == "fill":
        #pass # fill the machine
        fill_machine()
    elif option == "report":
        #pass # # print a report
        print_report()
    else:
        print("Try again!")












