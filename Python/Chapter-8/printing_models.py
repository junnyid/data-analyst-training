# Modifying a List in a function

# start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# #stimulate printing each design, until none are left
# #Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
# #Display all complete models
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# Organize with funtions
def print_models(unprinted_designs, complete_models):
    """Simulate printinhg each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        complete_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
complete_models = []

print_models(unprinted_designs, complete_models)
show_completed_models(complete_models)
