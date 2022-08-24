from dataclasses import dataclass, field

from typing import overload

import numpy as np

@dataclass
class Vec2D:
    x: float = field(
        default = 0.
    )

    y: float = field(
        default = 0.
    )

    @property
    def to_tuple(self) -> tuple:
        return (self.x, self.y)
    
    def __neg__(self):
        return type(self)(-self.x, -self.y)
    
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)
    
    def __mul__(self, c: float):
        return type(self)(self.x * c, self.y * c)
    
    def __truediv__(self, c: float):
        if c == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return type(self)(self.x / c, self.y / c)

    def __abs__(self):
        return type(self)(abs(self.x), abs(self.y))

    def __pow__(self, p: float):
        return type(self)(self.x ** p, self.y ** p)
    
    __rmul__ = __mul__
    __rdiv__ = __truediv__

    def lp_norm(self, p: int, radical: bool = True) -> float:
        if radical:
            return sum((abs(self) ** p).to_tuple) ** (1 / p)
        return sum((abs(self) ** p).to_tuple)

    def normalise(self):
        norm = self.lp_norm(p = 2)
        self.x /= norm
        self.y /= norm
        return type(self)(self.x, self.y)

    def reset_vector(self) -> None:
        self.x = 0.0
        self.y = 0.0

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}]"
    
    