from ingestion import load_raw_data

def test_load_raw_data():
    raw = load_raw_data()
    assert raw is not None