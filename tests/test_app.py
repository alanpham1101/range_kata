import pytest
import json
import operator
from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


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


def test_valid_request(client, members):
    res = client.post("/api/analyze-demography", json=members)
    assert res.status_code == 200

    data = res.get_json()
    assert len(data["Silent Generation"]) == 2
    assert ["David", "Frank"] == list(map(operator.itemgetter("name"), data["Silent Generation"]))

    assert len(data["Baby Boomers"]) == 1
    assert ["Alice"] == list(map(operator.itemgetter("name"), data["Baby Boomers"]))

    assert len(data["Generation Y"]) == 2
    assert ["Eve", "Josh"] == list(map(operator.itemgetter("name"), data["Generation Y"]))

    assert len(data["Generation Z"]) == 1
    assert ["Bob"] == list(map(operator.itemgetter("name"), data["Generation Z"]))

    assert len(data["Generation Alpha"]) == 1
    assert ["Charlie"] == list(map(operator.itemgetter("name"), data["Generation Alpha"]))


def test_invalid_request_param(client):
    res = client.post("/api/analyze-demography", json={"name": "Bob", "birthdate": "1999-5-12"})
    assert res.status_code == 400
    assert res.get_json()["error"] == "Expected a JSON array of members"


def test_invalid_request_param_missing_fields(client):
    res = client.post("/api/analyze-demography", json=[
        {"name": "Alice"},
        {"birthdate": "1999-5-12"},
        {"name": "Charlie", "birthdate": "1980-5-12"}
    ])
    assert res.status_code == 400
    assert res.get_json()["error"] == "Invalid format of member"
