import pandas as pd
import numpy as np


def encode_ordinal(df: pd.DataFrame, categories: dict):
    encoded = {}
    for col in df:
        category = categories[col]

        def encode(series: pd.Series):
            return series.map(category)

        encoded_series = encode(df[col])
        encoded[col] = encoded_series
    return pd.DataFrame(encoded)


def get_weight_of_evidence(
    feature_col: str,
    target_col: str,
    df: pd.DataFrame,
) -> dict:
    """Assume binary variable `target_col`

    Parameters
    ----------
    feature_col : str
        [description]
    target_col : str
        [description]
    df : pd.DataFrame
        [description]

    Returns
    -------
    dict
        [description]
    """
    mask_missing_values = df[feature_col].isnull()
    df_missing = df[mask_missing_values]

    aggregate_cfg = {target_col: ["count", "sum"]}
    df_weight_of_evidence = df.groupby(feature_col).agg(aggregate_cfg)
    df_weight_of_evidence.columns = ["Count", "Event"]
    df_weight_of_evidence["perc"] = (
        df_weight_of_evidence["Count"] / df_weight_of_evidence["Count"].sum()
    )
    df_weight_of_evidence["Non_event"] = (
        df_weight_of_evidence["Count"] - df_weight_of_evidence["Event"]
    )
    df_weight_of_evidence["odd_i"] = (
        df_weight_of_evidence["Event"] / df_weight_of_evidence["Non_event"]
    )

    overall_event = df_weight_of_evidence["Event"].sum()
    overall_non_event = df_weight_of_evidence["Non_event"].sum()
    overall_odd = overall_event / overall_non_event

    df_weight_of_evidence["woe"] = np.log(df_weight_of_evidence["odd_i"] / overall_odd)

    df_missing_summary = pd.DataFrame()

    if len(df_missing) != 0:
        df_missing_summary = df_missing.agg({target_col: ["count", "sum"]}).T
        df_missing_summary["Non_event"] = (
            df_missing_summary["count"] - df_missing_summary["sum"]
        )
        df_missing_summary["odd_i"] = (
            df_missing_summary["sum"] / df_missing_summary["Non_event"]
        )
        df_missing_summary["woe"] = np.log(df_missing_summary["odd_i"] / overall_odd)

    IV = (
        (
            df_weight_of_evidence["Event"] / overall_event
            - df_weight_of_evidence["Non_event"] / overall_non_event
        )
        * df_weight_of_evidence["woe"]
    ).sum()

    return {
        "df_weight_of_evidence": df_weight_of_evidence,
        "IV": IV,
        "missing": df_missing_summary,
    }
