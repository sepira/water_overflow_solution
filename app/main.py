import argparse
from typing import List


class Glass:
    def __init__(self, capacity: int, fill_level: int = 0) -> None:
        self.capacity = capacity
        self.fill_level = fill_level

    def fill_remainder(self) -> float:
        """
        check if there is water left and let that be the remainder of the fill
        """
        return self.fill_level - self.capacity

    def is_full(self) -> bool:
        """
        returns True if the capacity has been filled or over-filled else return False
        """
        if self.fill_level >= self.capacity:
            return True
        return False


def calculate_water_level(poured) -> List[List[Glass]]:
    capacity = 250
    water_left = int(poured * 1000)  # L to mL conversion
    max_row = water_left // capacity
    # assumed that we can generate the glass tower until we reach the max_row
    glass_tower = [[Glass(capacity=capacity) for _ in range(j + 1)] for j in range(max_row)]
    glass_tower[0][0].fill_level = water_left
    row = 0

    while row < max_row and water_left > capacity:
        for tmp_glass_pos in range(row):
            tmp_row = row - 1
            if glass_tower[tmp_row][tmp_glass_pos].is_full():
                fill_remainder = glass_tower[tmp_row][tmp_glass_pos].fill_remainder()
                glass_tower[tmp_row][tmp_glass_pos].fill_level = capacity
                glass_tower[tmp_row + 1][tmp_glass_pos].fill_level += fill_remainder / 2.0
                glass_tower[tmp_row + 1][tmp_glass_pos + 1].fill_level += fill_remainder / 2.0
                water_left -= capacity
        row += 1
    return glass_tower


def greet(name: str) -> str:
    return f'Hi, {name}!'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="a CLI that takes an amount of water to be poured, "
                                                 "and the row and glass position to return how"
                                                 "much liquid is in the j'th glass of the i'th row "
                                                 "when K litres are poured into the top most glass ")
    parser.add_argument('--poured', type=float,
                        help='a floating number representing K litres to be poured in the glass')
    parser.add_argument('--row', type=int,
                        help='an int number representing ith row of the glass')
    parser.add_argument('--glass', type=int,
                        help='an int number representing jth position of the glass')
    args = parser.parse_args()

    glass_tower = calculate_water_level(args.poured)
    query_fill_level = glass_tower[args.row][args.glass].fill_level

    print(f'When poured {args.poured} litres of water, the liquid in row {args.row} '
          f'of glass {args.glass} is {query_fill_level} mL')
