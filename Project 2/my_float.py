from __future__ import annotations

import sys
from dataclasses import dataclass


@dataclass
class Float(float):
    def __new__(self, value):
        return float.__new__(self, value)

    def __init__(self, value):
        float.__init__(value)

    def __eq__(self, other: Float) -> bool:
        return abs(float(self) - other) <= sys.float_info.epsilon

    def __lt__(self, other: Float) -> bool:
        return not (self == other) and float(self) < other

    def __le__(self, other: Float) -> bool:
        return self < other or self == other
    
    def __gt__(self, other: Float) -> bool:
        return not (self <= other)
    
    def __ge__(self, other: Float) -> bool:
        return not (self < other)

    def __str__(self) -> str:
        return f'Float({float(self)})'
