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


def greet(name):
    return f'Hi, {name}!'
