#Andrew Hilton 3/1/18
def inventory():
    inventory = {'apples': 10, 'bananas': 20, 'oranges': 30, 'pears': 50} #Creates dictionary to call from
    print(inventory)
    choice=input("What do you want to change?")
    ammount=input("How much do you want to remove?") #Recieves inputs
    ammount = int(ammount)
    if choice == "bananas":
        inventory['bananas'] = inventory['bananas'] - ammount #Beautiful if tree :-)
        print(inventory)
    elif choice == "apples":
        inventory['apples'] = inventory['apples'] - ammount
        print(inventory)
    elif choice == "oranges":
        inventory['oranges'] = inventory['oranges'] - ammount
        print(inventory)
    elif choice == "pears":
        inventory['pears'] = inventory['pears'] - ammount
        print(inventory)
    else:
        print("Error") #For improper inputs or no input
        inventory()
inventory()
    
