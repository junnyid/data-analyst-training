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



class Admin(User):
    def __init__(self, first_name, last_name, nickname, email, number_phone):
        super().__init__(first_name, last_name, nickname, email, number_phone)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        return self.privileges
    

junny = Admin('Junny', 'Nguy', 'Ang', 'angangvippro@gmail.com', +8412345678)
junny.describe_user()
junny.greet_user()
print(junny.show_privileges())