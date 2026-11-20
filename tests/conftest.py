import pytest

from orderlab.csv_report import revenue_from_csv


@pytest.fixture
def sample_csv(tmp_path):
    path = tmp_path / "sample.csv"
    path.write_text("price,quantity\n10000,2\n5000,3\n", encoding="utf-8")
    return path


def test_fixture_revenue(sample_csv):
    assert revenue_from_csv(sample_csv) == 0
