import pandas as pd
import pytest
import sys
sys.path.append("scripts")
from data_quality import check_data_quality

def test_data_quality_passes_with_good_data(tmp_path):
    good_df = pd.DataFrame({
        "tenure": [12, 24],
        "MonthlyCharges": [50.0, 70.0],
        "TotalCharges": [600.0, 1680.0],
        "Churn": [0, 1]
    })
    filepath = tmp_path / "good_data.csv"
    good_df.to_csv(filepath, index=False)
    assert check_data_quality(str(filepath)) == True

def test_data_quality_fails_with_empty_data(tmp_path):
    empty_df = pd.DataFrame()
    filepath = tmp_path / "empty.csv"
    empty_df.to_csv(filepath, index=False)
    with pytest.raises(SystemExit):
        check_data_quality(str(filepath))

def test_data_quality_fails_with_missing_column(tmp_path):
    bad_df = pd.DataFrame({
        "tenure": [12],
        "MonthlyCharges": [50.0]
    })
    filepath = tmp_path / "bad.csv"
    bad_df.to_csv(filepath, index=False)
    with pytest.raises(SystemExit):
        check_data_quality(str(filepath))

        