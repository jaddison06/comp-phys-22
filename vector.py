from dataclasses import dataclass
from math import sqrt

@dataclass
class V2:
    x: float
    y: float

    def dst(self, other: 'V2') -> float:
        return sqrt(
            ((self.x - other.x) ** 2) +
            ((self.y - other.y) ** 2)
        )

    def __add__(self, other: 'V2') -> 'V2':
        return V2(self.x + other.x, self.y + other.y)