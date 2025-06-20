# Using a while Loop with Lists and Dictionaries

# Moving items from One List to Another
# start with users that need to be verified
# add an empty list to hold confirmed users.
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

# verify each user until there are no more unconfirmed users.
# move each verified user into the list of confirmed users.
while unconfirmed_users:  # the list is not empty
    current_user = unconfirmed_users.pop()  # pop() remove

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
