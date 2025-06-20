prompt = "\nYou enter toppings for your pizza: "
prompt += "\nEnter 'quit' when you finish pizza. "

pizza = ""
while pizza != "quit":
    pizza = input(prompt)
    if pizza != "quit":
        print(pizza)
