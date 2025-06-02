def build_profile(first, last, **user_info):    #**user_info: create a dictionary
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('alert', 'einstein', location='princeton', field='physics')

print(user_profile)