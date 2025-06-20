from pathlib import Path
import json

from matplotlib.style import use


def get_stored_user_info(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    return None


def get_new_user_info(path):
    """Prompt for a new username."""
    name = input("What is your name? ")
    age = input("How old are you? ")
    country = input("Where are you from? ")

    user_info = {"name": name, "age": age, "country": country}
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user by name."""
    path = Path("user_info.json")
    user_info = get_stored_user_info(path)

    if user_info:
        confirm = input(f"Is this you, {user_info['name']}? (y/n): ").strip().lower()
        if confirm != "y":
            user_info = get_new_user_info(path)
            print(
                f"Thank you, {user_info['name']}! I'll remember you in the next time."
            )
        else:
            print(f"Welcome back, {user_info['name']}!")
    else:
        user_info = get_new_user_info(path)
        print(f"hank you, {user_info['name']}! I'll remember you in the next time.")

    # Display the remember info
    print("Here's what I remember your informations:")
    print(f" - Name: {user_info['name']}")
    print(f" - Age: {user_info['age']}")
    print(f" - Country: {user_info['country']}")


greet_user()
