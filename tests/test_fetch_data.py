import pytest
from src.fetch_data import fetch_data

def test_fetch_data():
    response = fetch_data("2023-01-01", "2023-01-02")
    assert response.rows, "No rows fetched from GA4 API"
