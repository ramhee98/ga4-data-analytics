import pytest
from src.process_data import response_to_dataframe
from src.fetch_data import fetch_data

def test_response_to_dataframe():
    response = fetch_data("2023-01-01", "2023-01-02")
    df = response_to_dataframe(response)
    assert not df.empty, "DataFrame is empty"
