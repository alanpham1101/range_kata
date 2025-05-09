from dataclasses import dataclass
from typing import Union

Number = Union[int, float]


@dataclass(frozen=True)
class Range:
    _lower: Number
    _upper: Number
    _include_lower: bool
    _include_upper: bool

    @staticmethod
    def __create(
        lower: Number, upper: Number, include_lower: bool, include_upper: bool
    ) -> 'Range':
        if lower > upper:
            raise ValueError("lower must not be greater than upper")
        return Range(lower, upper, include_lower, include_upper)

    @classmethod
    def open(cls, lower: Number, upper: Number) -> None:
        return cls.__create(lower, upper, False, False)

    @classmethod
    def closed(cls, lower: Number, upper: Number) -> None:
        return cls.__create(lower, upper, True, True)

    @classmethod
    def open_closed(cls, lower: Number, upper: Number) -> None:
        return cls.__create(lower, upper, False, True)

    @classmethod
    def closed_open(cls, lower: Number, upper: Number) -> None:
        return cls.__create(lower, upper, True, False)

    @classmethod
    def less_than(cls, num: Number) -> None:
        return cls.__create(float("-inf"), num, False, False)

    @classmethod
    def greater_than(cls, num: Number) -> None:
        return cls.__create(num, float("inf"), False, False)

    @classmethod
    def at_least(cls, num: Number) -> None:
        return cls.__create(num, float("inf"), True, False)

    @classmethod
    def at_most(cls, num: Number) -> None:
        return cls.__create(float("-inf"), num, False, True)

    @classmethod
    def all(cls) -> None:
        return cls.__create(float("-inf"), float("inf"), False, True)

    def contains(self, value: Number) -> bool:
        return all([
            value >= self._lower if self._include_lower else value > self._lower,
            value <= self._upper if self._include_upper else value < self._upper
        ])
