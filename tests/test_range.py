import pytest
from range import Range


def test_invalid_range():
    with pytest.raises(ValueError):
        Range.open(30, 20)

    with pytest.raises(ValueError):
        Range.closed(35, 15)

    with pytest.raises(ValueError):
        Range.open_closed(100, 50)

    with pytest.raises(ValueError):
        Range.closed_open(80, 40)


def test_valid_open_range():
    range = Range.open(10, 50)

    assert range.contains(5) is False
    assert range.contains(10) is False
    assert range.contains(25) is True
    assert range.contains(50) is False
    assert range.contains(51) is False


def test_valid_closed_range():
    range = Range.closed(10, 50)

    assert range.contains(5) is False
    assert range.contains(10) is True
    assert range.contains(25) is True
    assert range.contains(50) is True
    assert range.contains(51) is False


def test_valid_open_closed_range():
    range = Range.open_closed(10, 50)

    assert range.contains(5) is False
    assert range.contains(10) is False
    assert range.contains(25) is True
    assert range.contains(50) is True
    assert range.contains(51) is False


def test_valid_closed_open_range():
    range = Range.closed_open(10, 50)

    assert range.contains(5) is False
    assert range.contains(10) is True
    assert range.contains(25) is True
    assert range.contains(50) is False
    assert range.contains(51) is False


def test_valid_less_than_range():
    range = Range.less_than(10)

    assert range.contains(float("-inf")) is False
    assert range.contains(-10e6) is True
    assert range.contains(9.0) is True
    assert range.contains(10.0) is False
    assert range.contains(11.0) is False


def test_valid_greater_than_range():
    range = Range.greater_than(10)

    assert range.contains(float("-inf")) is False
    assert range.contains(10.0) is False
    assert range.contains(11.0) is True
    assert range.contains(10e6) is True
    assert range.contains(float("-inf")) is False


def test_valid_at_least_range():
    range = Range.at_least(20)

    assert range.contains(float("-inf")) is False
    assert range.contains(19.0) is False
    assert range.contains(20.0) is True
    assert range.contains(10e6) is True
    assert range.contains(float("-inf")) is False


def test_valid_at_most_range():
    range = Range.at_most(20)

    assert range.contains(float("-inf")) is False
    assert range.contains(-10e6) is True
    assert range.contains(19.0) is True
    assert range.contains(20.0) is True
    assert range.contains(float("-inf")) is False


def test_valid_all_range():
    range = Range.all()

    assert range.contains(float("-inf")) is False
    assert range.contains(-10e6) is True
    assert range.contains(0) is True
    assert range.contains(10e6) is True
    assert range.contains(float("-inf")) is False
