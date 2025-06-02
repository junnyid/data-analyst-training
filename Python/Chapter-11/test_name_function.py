from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Junny Archie' work?"""
    formatted_name = get_formatted_name('junny', 'archie')
    assert formatted_name == 'Junny Archie' 

def test_first_last_middle_name():
    """Do names like 'Junny Tulip Archie' work?"""
    formatted_name = get_formatted_name('junny', 'archie', 'tulip')
    assert formatted_name == 'Junny Tulip Archie'