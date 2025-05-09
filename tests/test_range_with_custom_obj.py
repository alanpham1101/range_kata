import pytest

from range_with_custom_obj import Range
from custom_object import DatetimeObject


def test_invalid_range():
    with pytest.raises(ValueError):
        Range.open(
            DatetimeObject("2024-08-30"), DatetimeObject("2023-08-29")
        )

    with pytest.raises(ValueError):
        Range.closed(
            DatetimeObject("2023-08-30"), DatetimeObject("2023-08-29")
        )

    with pytest.raises(ValueError):
        Range.open_closed(
            DatetimeObject("2023-09-30"), DatetimeObject("2023-08-29")
        )

    with pytest.raises(ValueError):
        Range.closed_open(
            DatetimeObject("2023-10-30"), DatetimeObject("2023-07-30")
        )


def test_valid_open_range():
    range = Range.open(
        DatetimeObject("2023-08-29"), DatetimeObject("2024-10-29")
    )

    assert range.contains(DatetimeObject("2023-08-29")) is False
    assert range.contains(DatetimeObject("2024-10-29")) is False
    assert range.contains(DatetimeObject("2024-09-29")) is True


def test_valid_closed_range():
    range = Range.closed(
        DatetimeObject("2023-08-29"), DatetimeObject("2024-10-29")
    )

    assert range.contains(DatetimeObject("2023-08-29")) is True
    assert range.contains(DatetimeObject("2024-10-29")) is True
    assert range.contains(DatetimeObject("2024-09-29")) is True


def test_valid_open_closed_range():
    range = Range.open_closed(
        DatetimeObject("2023-08-29"), DatetimeObject("2024-10-29")
    )

    assert range.contains(DatetimeObject("2023-08-29")) is False
    assert range.contains(DatetimeObject("2024-10-29")) is True
    assert range.contains(DatetimeObject("2024-09-29")) is True


def test_valid_closed_open_range():
    range = Range.closed_open(
        DatetimeObject("2023-08-29"), DatetimeObject("2024-10-29")
    )

    assert range.contains(DatetimeObject("2023-08-29")) is True
    assert range.contains(DatetimeObject("2024-10-29")) is False
    assert range.contains(DatetimeObject("2024-09-29")) is True


def test_valid_less_than_range():
    range = Range.less_than(DatetimeObject("2023-08-29"))

    assert range.contains(DatetimeObject("2020-08-29")) is True
    assert range.contains(DatetimeObject("2023-04-29")) is True
    assert range.contains(DatetimeObject("2023-08-29")) is False


def test_valid_greater_than_range():
    range = Range.greater_than(DatetimeObject("2023-08-29"))

    assert range.contains(DatetimeObject("2023-04-25")) is False
    assert range.contains(DatetimeObject("2023-08-29")) is False
    assert range.contains(DatetimeObject("2024-08-29")) is True


def test_valid_at_least_range():
    range = Range.at_least(DatetimeObject("2023-08-29"))

    assert range.contains(DatetimeObject("2023-04-25")) is False
    assert range.contains(DatetimeObject("2023-08-29")) is True
    assert range.contains(DatetimeObject("2024-08-29")) is True


def test_valid_at_most_range():
    range = Range.at_most(DatetimeObject("2023-08-29"))

    assert range.contains(DatetimeObject("2022-04-29")) is True
    assert range.contains(DatetimeObject("2023-08-29")) is True
    assert range.contains(DatetimeObject("2024-08-29")) is False


def test_valid_all_range():
    range = Range.all(DatetimeObject)

    assert range.contains(DatetimeObject("2022-04-29")) is True
    assert range.contains(DatetimeObject("2023-08-29")) is True
    assert range.contains(DatetimeObject("2024-08-29")) is True
