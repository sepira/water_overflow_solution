from water_overflow_solution.app.main import greet


def test_greet():
    name = 'James'
    assert greet(name) == 'Hi, James!'
