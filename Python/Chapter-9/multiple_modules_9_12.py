from privileges_9_8 import Admin

junny = Admin("Junny", "Nguy", "Ang", "angangvippro@gmail.com", +8412345678)
junny.describe_user()

junny.privileges.show_privileges()
junny_privileges = [
    "can add posts",
    "can remove posts",
    "can suspend accounts",
]
junny.privileges.show_privileges = junny_privileges
print(f"\nThe admin {junny.nickname} has these privileges:")
