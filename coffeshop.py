print("Hello,Welcome To Coffeshop")

name = input("What is your name?\n")

print(name)
print("Wellcome To My Coffeshop " + name +
      ",Thank you so much for coming in today.\n\n\n")

menu = ("Black Coffe, Charcoal coffee, Expresso, Latte, Cappucino\n")

print(name + ",What would you like from menu today?\n" + menu)

order = input()
price = 10
quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you " + name + " Your Total is : $" + str(total))

print("Whoa Sounds good " + name + ",we'll have your " + quantity + " " +
      order + " Ready for you in a moment")
