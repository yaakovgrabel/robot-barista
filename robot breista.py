#lets blild a robaot barista 

print("\n\n\nHello welcome to yaakov coffee!!!!!!!!!!!!!!!!")
name = input("what is your name?\n")

#if evil ben is here kick him out

if name == "ben" or name == "BEN" or name == "Ben" or name == "shalev":
    evil_status = input("are you evil?\n")
    if evil_status == "yes":
        print("get out evil"  + name +  " you are not welcome here!!!!!!")
        exit()
    print("oh so you are one of those good " + name +" i see.... well welcome " + name + "\n\n\n")
else:
    print("Hello " + name +" ,\nthank you so much for coming in today\n\n\n")


#menu display

menu = "black coffee, cappuccino, espresso, latte, frappuccino"


print(name + "what would you like form our menu? here is what we are serving.\n" + menu)
order = input()
    
if order == "frappuccino":
    price = 13
elif order == "black coffee":
    price = 3
elif order == "cappuccino":
    price = 10
elif order == "espresso":
    price = 5
elif order == "latte":
    price = 9
    



while True:
    quantity = int(input("how many coffees would you like\n"))

    if quantity <= 0:
        print("sorry you cant order less than 1 coffee")
    else:
        #total calculation
        total = price * quantity
        break

print("thank you. your total is: $" + str(total))

print("sounds good " + name + " we will have your " + str(quantity) + " " + order + " ready for you in a momnet")



