users = ["benson", "john", "david", "admin", "sheldon"]
for user in users:
    if user == "admin":
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for your logging in again")
