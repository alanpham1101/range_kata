from dataclasses import dataclass
from typing import Union

from custom_object import IntObject, FloatObject, CharObject, DatetimeObject

Obj = Union[IntObject, FloatObject, CharObject, DatetimeObject]


@dataclass(frozen=True)
class Range:
    _lower: Obj
    _upper: Obj
    _include_lower: bool
    _include_upper: bool

    @staticmethod
    def __create(
        lower: Obj, upper: Obj, include_lower: bool, include_upper: bool
    ) -> 'Range':
        if lower > upper:
            raise ValueError("lower must not be greater than upper")
        return Range(lower, upper, include_lower, include_upper)

    @classmethod
    def open(cls, lower: Obj, upper: Obj) -> None:
        return cls.__create(lower, upper, False, False)

    @classmethod
    def closed(cls, lower: Obj, upper: Obj) -> None:
        return cls.__create(lower, upper, True, True)

    @classmethod
    def open_closed(cls, lower: Obj, upper: Obj) -> None:
        return cls.__create(lower, upper, False, True)

    @classmethod
    def closed_open(cls, lower: Obj, upper: Obj) -> None:
        return cls.__create(lower, upper, True, False)

    @classmethod
    def less_than(cls, obj: Obj) -> None:
        return cls.__create(obj.get_lowest_bound(), obj, False, False)

    @classmethod
    def greater_than(cls, obj: Obj) -> None:
        return cls.__create(obj, obj.get_uppermost_bound(), False, False)

    @classmethod
    def at_least(cls, obj: Obj) -> None:
        return cls.__create(obj, obj.get_uppermost_bound(), True, False)

    @classmethod
    def at_most(cls, obj: Obj) -> None:
        return cls.__create(obj.get_lowest_bound(), obj, False, True)

    @classmethod
    def all(cls, obj_type: Obj) -> None:
        return cls.__create(
            obj_type.get_lowest_bound(), obj_type.get_uppermost_bound(), False, True
        )

    def contains(self, value: Obj) -> bool:
        return all([
            value >= self._lower if self._include_lower else value > self._lower,
            value <= self._upper if self._include_upper else value < self._upper
        ])
