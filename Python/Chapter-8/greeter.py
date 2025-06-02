#FUNCTIONS
#defining a function
def greet_user():                       
    """Display a simple greeting."""
    print("Hello!")
greet_user()

#Passing Information to a Function
def greet_user(username):   
    """"Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')
greet_user('sarah')

#argument and parameters: in this case the argument 'jesse' 'sarah' was passed to the function greet_user(),
#and the value was assigned to the parameter username
