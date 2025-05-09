from dataclasses import dataclass


@dataclass(frozen=True)
class Range:
    _lower: int
    _upper: int

    @classmethod
    def of(cls, lower: int, upper: int) -> None:
        if lower > upper:
            raise ValueError("Lower must be less than or equal to upper")
        return cls(lower, upper)

    def contains(self, value: int) -> bool:
        return self._lower <= value <= self._upper
