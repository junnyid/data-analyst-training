def make_shirt(size, text):
    print(f"The size of shirt is {size}.")
    print(f"In shirt have a text: {text}")


make_shirt("M", "I love Python")


# default
def make_shirt(text, size="large"):
    print(f"The size of shirt is {size}.")
    print(f"In shirt have a text: {text}")


make_shirt("I love Python")
