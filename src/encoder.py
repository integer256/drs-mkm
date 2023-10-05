import numpy as np
import pandas as pd
import category_encoders as ce


def encode(train_values, test_values):
    """
    Encode the train and test data using binary encoding.

    Args:
        train_values (DataFrame): The training data.
        test_values (DataFrame): The test data.

    Returns:
        tuple: A tuple containing the encoded train and test data.
    """
    train_values = binary_encode(train_values)
    test_values = binary_encode(test_values)

    return (train_values, test_values)


def binary_encode(df):
    """
    Binary encode the given dataframe.

    Args:
        df (DataFrame): The dataframe to be binary encoded.

    Returns:
        DataFrame: The binary encoded dataframe.
    """
    cols = [
        'ground_floor_type', 'land_surface_condition', 'foundation_type', 'roof_type', 
        'other_floor_type', 'position', 'plan_configuration', 'legal_ownership_status', 'geo_level_1_id', 
        'geo_level_2_id', 'geo_level_3_id']
    encoder = ce.BinaryEncoder(cols=cols)
    binary_encoded = encoder.fit_transform(df)
    return binary_encoded
