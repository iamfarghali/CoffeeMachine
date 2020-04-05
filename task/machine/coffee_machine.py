class CoffeeMachine:
    def __init__(self, init_water=400, init_milk=540, init_beans=120, init_money=550, init_cups=9):
        self.current_water = init_water
        self.current_milk = init_milk
        self.current_beans = init_beans
        self.current_money = init_money
        self.current_cups = init_cups

    # Represent status of the machine
    def machine_status(self):
        print('The coffee machine has:')
        print(f'{self.current_water} of water')
        print(f'{self.current_milk} of milk')
        print(f'{self.current_beans} of coffee beans')
        print(f'{self.current_cups} of disposable cups')
        print(f'${self.current_money} of money')
        print()

    # Making coffee depends on its type
    def make_coffee(self, coffee_type):
        message = ''
        if coffee_type == 1:
            message = self.espresso()
        elif coffee_type == 2:
            message = self.latte()
        elif coffee_type == 3:
            message = self.cappuccino()
        return message

    # Buy a coffee
    def buy(self, option):
        if option == 'back':
            return 'back'
        return self.make_coffee(int(option))

    # Fill machine
    def fill(self):
        self.current_water += int(input('Write how many ml of water do you want to add:\n').strip())
        self.current_milk += int(input('Write how many ml of milk do you want to add:\n').strip())
        self.current_beans += int(input('Write how many grams of coffee beans do you want to add:\n').strip())
        self.current_cups += int(input('Write how many disposable cups of coffee do you want to add:\n').strip())
        print()

    # Take machine's money
    def take(self):
        gave_you = self.current_money
        self.current_money = 0
        return f'\nI gave you ${gave_you}\n'

    # Coffee Types
    def espresso(self):
        if self.current_water < 250:
            return 'Sorry, not enough water!'
        elif self.current_beans < 16:
            return 'Sorry, not enough coffee beans!'
        elif self.current_cups < 1:
            return 'Sorry, not enough disposable cups!'
        self.current_water -= 250
        self.current_beans -= 16
        self.current_cups -= 1
        self.current_money += 4
        return 'I have enough resources, making you a coffee!'

    def latte(self):
        if self.current_water < 350:
            return 'Sorry, not enough water!'
        elif self.current_milk < 75:
            return 'Sorry, not enough milk!'
        elif self.current_beans < 20:
            return 'Sorry, not enough coffee beans!'
        elif self.current_cups < 1:
            return 'Sorry, not enough disposable cups!'
        self.current_water -= 350
        self.current_milk -= 75
        self.current_beans -= 20
        self.current_cups -= 1
        self.current_money += 7
        return 'I have enough resources, making you a coffee!'

    def cappuccino(self):
        if self.current_water < 200:
            return 'Sorry, not enough water!'
        elif self.current_milk < 100:
            return 'Sorry, not enough milk!'
        elif self.current_beans < 12:
            return 'Sorry, not enough coffee beans!'
        elif self.current_cups < 1:
            return 'Sorry, not enough disposable cups!'
        self.current_water -= 200
        self.current_milk -= 100
        self.current_beans -= 12
        self.current_cups -= 1
        self.current_money += 6
        return 'I have enough resources, making you a coffee!'


cm = CoffeeMachine()

while True:
    action = input('Write action (buy, fill, take, remaining, exit):\n').strip()
    if action == 'remaining':
        cm.machine_status()
    elif action == 'buy':
        msg = cm.buy(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n').strip())
        if msg == 'back':
            continue
        else:
            print(msg, '\n')
    elif action == 'fill':
        cm.fill()
    elif action == 'take':
        print(cm.take(), '\n')
    else:
        break
