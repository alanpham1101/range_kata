import pytest
import operator

from demography import analyze_member_demography


@pytest.fixture
def members():
    return [
        {"name": "Alice", "birthdate": "1950-5-12"},
        {"name": "Bob", "birthdate": "1999-5-12"},
        {"name": "Charlie", "birthdate": "2020-5-12"},
        {"name": "David", "birthdate": "1920-5-12"},
        {"name": "Eve", "birthdate": "1985-5-12"},
        {"name": "Frank", "birthdate": "1935-5-12"},
        {"name": "Josh", "birthdate": "1990-5-12"},
    ]


def test_analyze_member_demography(members):
    res = analyze_member_demography(members)

    assert len(res["Silent Generation"]) == 2
    assert ["David", "Frank"] == list(map(operator.itemgetter("name"), res["Silent Generation"]))

    assert len(res["Baby Boomers"]) == 1
    assert ["Alice"] == list(map(operator.itemgetter("name"), res["Baby Boomers"]))

    assert len(res["Generation Y"]) == 2
    assert ["Eve", "Josh"] == list(map(operator.itemgetter("name"), res["Generation Y"]))

    assert len(res["Generation Z"]) == 1
    assert ["Bob"] == list(map(operator.itemgetter("name"), res["Generation Z"]))

    assert len(res["Generation Alpha"]) == 1
    assert ["Charlie"] == list(map(operator.itemgetter("name"), res["Generation Alpha"]))
