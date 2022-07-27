import pandas as pd
import pytest


@pytest.mark.ut
def test_encode_ordinal_returns_correct_values():
    # Given
    from summer.preprocessing.encoding import encode_ordinal

    col = "col"
    df = pd.DataFrame({col: ["low", "med", "high"]})
    categories = {col: {"low": 0, "med": 1, "high": 2}}
    expected_df_encoded = pd.DataFrame({col: [0, 1, 2]})

    # When
    df_encoded = encode_ordinal(df, categories)

    # Given
    pd.testing.assert_frame_equal(df_encoded, expected_df_encoded)
