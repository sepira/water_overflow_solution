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


def greet(name):
    return f'Hi, {name}!'
