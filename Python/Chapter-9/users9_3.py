class User:

    def __init__(self, first_name, last_name, nickname, email, number_phone):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.nickname = nickname
        self.email = email
        self.number_phone = number_phone

    def describe_user(self):
        print(f"\nMy name is {self.first_name} {self.last_name}.")
        print(f"Everyone call me is {self.nickname}.")
        print(f"My email is {self.email}.")
        print(f"My number phone is {self.number_phone}")

    def greet_user(self):
        print(f"Bonjour, nice to meet you, {self.nickname}!")


junny = User("Junny", "Nguy", "Ang", "angangvippro@gmail.com", +8412345678)
junny.describe_user()
junny.greet_user()

dwingarium = User("Dungx", "Pham", "Blueberry", "dwingariumij@gmail.com", +8487654321)
dwingarium.describe_user()
dwingarium.greet_user()
