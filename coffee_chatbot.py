#BUILD CHATBOTS WITH PYTHON
#Coffee Chatbot
#But first, coffee.
#Whether it’s to get us ready to jump-start our day or to get us through a late-night cram session, many of us need our regular caffeine fix! Ordering coffee is just one example of a process that can be automated with the help of a chatbot.
#you’re given the task of creating a Python chatbot that can help cut the wait time of a normal coffee run by taking customers’ orders in advance. Write your code in the file called script.py and run it by entering python3 script.py in the terminal.
#Let’s get started

# script.py

# Task 1
def coffee_bot():
    print("Welcome to the cafe!")

# Task 2
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    return res

# Task 3
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

# Task 5
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

# Task 6
def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    return res

# Task 7
def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

# Task 8
def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
    return res

# Task 9
def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()

# Task 10
def get_drink_type():
    res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

# Task 11
def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    drink_type = get_drink_type()
    print(f"Alright, that's a {size} {drink_type}!")

# Task 12
def get_name():
    name = input("Can I get your name please? \n> ")
    return name

# Task 13
def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    drink_type = get_drink_type()
    print(f"Alright, that's a {size} {drink_type}!")
    name = get_name()
    print(f"Thanks, {name}! Your drink will be ready shortly.\nOrder complete!")

# Bonus Task
# You can add more functions for additional functionality (e.g., cup choice, hot/iced preference, additional orders)

# Run the chatbot
coffee_bot()
