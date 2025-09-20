import pytest
from main import Prime

@pytest.mark.parametrize("num,expected", [
    (1, False), 
    (3, False),
    (4, True),
    (5, False),
    (6, True),
    ])

def test_prime(num,expected):
    assert Prime (num) == expected