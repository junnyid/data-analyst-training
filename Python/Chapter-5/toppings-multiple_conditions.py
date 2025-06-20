# testing multiple conditions
# if you use if statement, then this test is run regardless whether the previous test passed or not
requested_toppings = ["mushroom", "extra cheese"]

if "mushroom" in requested_toppings:
    print("Adding mushroom.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
