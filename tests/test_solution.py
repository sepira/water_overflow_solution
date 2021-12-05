import pytest

from water_overflow_solution.app.main import greet, Glass


def test_greet():
    name = 'James'
    assert greet(name) == 'Hi, James!'


@pytest.mark.parametrize(
    "glass_input,expected",
    [
        (Glass(capacity=10, fill_level=10), True),
        (Glass(capacity=15, fill_level=10), False),
        (Glass(capacity=300, fill_level=400), True)
    ]
)
def test_glass_is_full(glass_input, expected):
    assert glass_input.is_full() == expected
