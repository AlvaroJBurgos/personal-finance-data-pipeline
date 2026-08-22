import pytest

from etl.ingestion import load_raw_data


def test_load_data_fails_with_empty_folder(monkeypatch):
    monkeypatch.setattr("etl.ingestion.os.listdir", lambda path: [])
    with pytest.raises(ValueError, match="No valid Excel files found"):
        load_raw_data()
