class User:

    def __init__(
        self, first_name, last_name, nickname, email, number_phone, login_attempts
    ):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.nickname = nickname
        self.email = email
        self.number_phone = number_phone
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"\nMy name is {self.first_name} {self.last_name}.")
        print(f"Everyone call me is {self.nickname}.")
        print(f"My email is {self.email}.")
        print(f"My number phone is {self.number_phone}")

    def greet_user(self):
        print(f"Bonjour, nice to meet you, {self.nickname}!")

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        print("You have attempted {} times to login".format(self.login_attempts))

    def reset_login_attempts(self, reset):
        if reset == 0 or reset == "reset":
            self.login_attempts = 0
            self.login_attempts = reset
            print("You reset the login attempts.")


junny = User("Junny", "Nguy", "Ang", "angangvippro@gmail.com", "+8412345678", 0)
junny.describe_user()
junny.greet_user()
junny.increment_login_attempts(1)
junny.increment_login_attempts(4)
print(junny.login_attempts)
junny.reset_login_attempts(0)
print(junny.login_attempts)
junny.increment_login_attempts(5)
junny.increment_login_attempts(5)
junny.reset_login_attempts(0)
print(junny.login_attempts)
junny.reset_login_attempts(0)
print(junny.login_attempts)


dwingarium = User(
    "Dungx", "Pham", "Blueberry", "dwingariumij@gmail.com", "+8487654321", 0
)
dwingarium.describe_user()
dwingarium.greet_user()
