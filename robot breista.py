# Let's build a robot barista 

print("\n\n\nHello welcome to yaakov coffee!!!!!!!!!!!!!!!!")
name = input("what is your name?\n")

#if evil Ben is here, kick him out

if name == "ben" or name == "BEN" or name == "Ben" or name == "shalev":
    evil_status = input("are you evil?\n")
    if evil_status == "no":
        print("oh so you are one of those good " + name +" i see.... well welcome " + name + "\n\n\n")
    else:
        good_deed = int(input("how many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deed < 4:
        print("get out evil "  + name +  " you are not welcome here!!!!!!")
        exit()
        
    elif evil_status == "yes" and good_deed >= 4:
        print("oh so you are one of those good " + name +" i see.... well welcome " + name + "\n\n")
        print("Hello " + name +" ,\nthank you so much for coming in today\n\n\n")
else:
    print("Hello " + name +" ,\nthank you so much for coming in today\n\n\n")

#menu display

menu = "black coffee, cappuccino, espresso, latte, frappuccino"


print(name + " what would you like form our menu? here is what we are serving.\n" + menu)
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
if order == "latte":
    whipped_cream = input("would you like whipped cream on that?\n")
    if whipped_cream == "yes":
        price += 1.5
        print("got it I have added whipped cream added")
    else:
        print("no whipped cream got it")

else:
    print("sorry we dont have that here")
    
    



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



