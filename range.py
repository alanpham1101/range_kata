from dataclasses import dataclass


@dataclass(frozen=True)
class Range:
    _lower: int
    _upper: int
    _include_lower: bool
    _include_upper: bool

    @staticmethod
    def __create(lower: int, upper: int, include_lower: bool, include_upper: bool) -> 'Range':
        if lower > upper:
            raise ValueError("lower must not be greater than upper")
        return Range(lower, upper, include_lower, include_upper)

    @classmethod
    def open(cls, lower: int, upper: int) -> None:
        return cls.__create(lower, upper, False, False)

    @classmethod
    def closed(cls, lower: int, upper: int) -> None:
        return cls.__create(lower, upper, True, True)

    @classmethod
    def open_closed(cls, lower: int, upper: int) -> None:
        return cls.__create(lower, upper, False, True)

    @classmethod
    def closed_open(cls, lower: int, upper: int) -> None:
        return cls.__create(lower, upper, True, False)

    def contains(self, value: int) -> bool:
        return all([
            value >= self._lower if self._include_lower else value > self._lower,
            value <= self._upper if self._include_upper else value < self._upper
        ])
