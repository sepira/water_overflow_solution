# water_overflow_solution
A CLI app that solves the water overflow problem



# Initializing the app
clone the repo

This assumes you have python3.7 and have poetry as a dependencey package, if not run:

``pip install poetry``

``poetry shell``

# Running the test

``poetry run pytest``

# Running the app

``python app/main.py --poured {float_num} --row {int_num} --glass {int_num}``

```
usage: main.py [-h] [--poured POURED] [--row ROW] [--glass GLASS]

a CLI that takes an amount of water to be poured, and the row and glass
position to return howmuch liquid is in the j'th glass of the i'th row when K
litres are poured into the top most glass

arguments:
  -h, --help       show this help message and exit
  --poured POURED  a floating number representing K litres to be poured in the
                   glass
  --row ROW        an int number representing ith row of the glass
  --glass GLASS    an int number representing jth position of the glass
```