class Coffee_Machine():
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def state(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee_beans) + " of coffee beans")
        print(str(self.cups) + " of cups")
        print(str(self.money) + " of money")

    def buy(self):
        option_b = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if option_b == "1":
            if (self.water < 250 or self.coffee_beans < 16 or self.cups < 1):
                if self.water < 250:
                    print("Sorry, not enough water!")
                if self.coffee_beans < 16:
                    print("Sorry, not enough coffee beans!")
                if self.coffee_beans < 1:
                    print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee_beans -= 16
                self.cups -= 1
                self.money += 4
        if option_b == "2":
            if (self.water < 350 or self.milk < 75 or self.coffee_beans < 20 or self.cups < 1):
                if self.water < 350:
                    print("Sorry, not enough water!")
                if self.milk < 75:
                    print("Sorry, not enough milk!")
                if self.coffee_beans < 20:
                    print("Sorry, not enough coffee beans!")
                if self.coffee_beans < 1:
                    print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
        if option_b == "3":
            if (self.water < 200 or self.milk < 100 or self.coffee_beans < 12 or self.cups < 1):
                if self.water <200:
                    print("Sorry, not enough water!")
                if self.milk < 100:
                    print("Sorry, not enough milk!")
                if self.coffee_beans < 12:
                    print("Sorry, not enough coffee beans!")
                if self.coffee_beans < 1:
                    print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
    def fill(self):
        add_water = int(input("Write how many ml of water do you want to add:\n"))
        add_milk = int(input("Write how many ml of milk do you want to add:\n"))
        add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

        self.water += add_water
        self.milk += add_milk
        self.coffee_beans += add_beans
        self.cups += add_cups

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0


coffee_machine = Coffee_Machine(400, 540, 120, 9, 550)
option = input("Write action (buy, fill, take, remaining, exit):\n")
while option != "exit":
    if option == "remaining":
        coffee_machine.state()
        option = input("Write action (buy, fill, take, remaining, exit):\n")
    if option == "buy":
        coffee_machine.buy()
        option = input("Write action (buy, fill, take, remaining, exit):\n")
    if option == "back":
        pass
        option = input("Write action (buy, fill, take, remaining, exit):\n")
    elif option == "fill":
        coffee_machine.fill()
        option = input("Write action (buy, fill, take, remaining, exit):\n")
    elif option == "take":
        coffee_machine.take()
        option = input("Write action (buy, fill, take, remaining, exit):\n")
    elif option == "exit":
        break





