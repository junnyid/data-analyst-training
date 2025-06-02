import pytest

from employee import Employee

@pytest.fixture
def employee():
    employee = Employee('junny', 'archie', 57_000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.salary == 62_000

def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.salary == 67_000
    
""" hOW TO TEST:
cd chapter-11/11-3_employee
pytest test_employee.py
"""