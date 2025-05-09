import pytest
from range import Range


def test_invalid_range():
    with pytest.raises(ValueError):
        Range.of(50, 10)


def test_valid_range():
    range = Range.of(10, 50)

    assert range.contains(5) is False
    assert range.contains(10) is True
    assert range.contains(25) is True
    assert range.contains(50) is True
