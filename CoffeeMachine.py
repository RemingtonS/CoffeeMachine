class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.dollars = 550
        self.espresso_water = 250
        self.espresso_beans = 16
        self.latte_water = 350
        self.latte_milk = 75
        self.latte_beans = 20
        self.cappuccino_water = 200
        self.cappuccino_milk = 100
        self.cappuccino_beans = 12

    def print_resources(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.coffee_beans))
        print("{} of disposable cups".format(self.disposable_cups))
        print("${} of money".format(self.dollars))

    def make_coffee(self, coffee_type):
        print("I have enough resources, making you a coffee!")
        # 1 = espresso - 250 ml of water, 16 g of coffee beans, $4
        # 2 = latte - 350 ml of water, 75 ml of milk, 20 g of coffee beans, $7
        # 3 = cappuccino - 200 ml of water, 100 ml of milk, 12 g of coffee, $6
        self.disposable_cups -= 1

        if coffee_type == "1":
            self.water -= 250
            self.coffee_beans -= 16
            self.dollars += 4
        elif coffee_type == "2":
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.dollars += 7
        elif coffee_type == "3":
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.dollars += 6

    def check_amounts(self, type_coffee):
        # 1 = espresso - 250 ml of water, 16 g of coffee beans, $4
        # 2 = latte - 350 ml of water, 75 ml of milk, 20 g of coffee beans, $7
        # 3 = cappuccino - 200 ml of water, 100 ml of milk, 12 g of coffee, $6
        if self.disposable_cups >= 1:
            if type_coffee == "1":
                if self.water < self.espresso_water:
                    print("Sorry, not enough water!")
                elif self.coffee_beans < self.espresso_beans:
                    print("Sorry, not enough coffee beans!")
                else:
                    self.make_coffee(type_coffee)
            elif type_coffee == "2":
                if self.water < self.latte_water:
                    print("Sorry, not enough water!")
                elif self.milk < self.latte_milk:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < self.latte_beans:
                    print("Sorry, not enough coffee beans!")
                else:
                    self.make_coffee(type_coffee)
            elif type_coffee == "3":
                if self.water < self.cappuccino_water:
                    print("Sorry, not enough water!")
                elif self.milk < self.cappuccino_milk:
                    print("Sorry, not enough milk!")
                elif self.coffee_beans < self.cappuccino_beans:
                    print("Sorry, not enough coffee beans!")
                else:
                    self.make_coffee(type_coffee)
        else:
            print("Sorry, not enough disposable cups!")

    def buy_coffee(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee_type == "1" or "2" or "3":
            self.check_amounts(coffee_type)
        elif coffee_type == "back":
            return

    def fill_machine(self):
        ml_water = int(input("Write how many ml of water do you want to add:"))
        ml_milk = int(input("Write how many ml of milk do you want to add:"))
        g_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        num_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.water += ml_water
        self.milk += ml_milk
        self.coffee_beans += g_beans
        self.disposable_cups += num_cups

    def take_money(self):
        print("I gave you ${}".format(self.dollars))
        self.dollars = 0

    def choose_action(self):
        action = input("Write action (buy, fill, take, remaining, exit):")
        while action != "exit":
            if action == "buy":
                self.buy_coffee()
            elif action == "fill":
                self.fill_machine()
            elif action == "take":
                self.take_money()
            elif action == "remaining":
                self.print_resources()
            action = input("Write action (buy, fill, take, remaining, exit):")


coffee_machine = CoffeeMachine()
coffee_machine.choose_action()
