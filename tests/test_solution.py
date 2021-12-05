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


def test_calculate_water_level():
    glass_tower = calculate_water_level(2)
    assert glass_tower[0][0].fill_level == 250
    assert glass_tower[1][0].fill_level == 250
    assert glass_tower[1][1].fill_level == 250
    assert glass_tower[2][0].fill_level == 250
    assert glass_tower[2][1].fill_level == 250
    assert glass_tower[3][0].fill_level == 31.25
    assert glass_tower[3][1].fill_level == 218.75
    assert glass_tower[3][3].fill_level == 31.25
