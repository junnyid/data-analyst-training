current_users = ['panda', 'doraemon', 'nobita', 'shisuka', 'doremi']

new_users = ['luffy', 'doremi', 'nami', 'franky', 'doraemon']

for new_user in new_users:
    if new_user in current_users:
        print("The person will need to enter a new username.")
    else:
        print("The usename is available")
