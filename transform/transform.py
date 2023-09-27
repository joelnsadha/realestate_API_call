import pandas as pd
import numpy as np
import datetime
from extract.extract import extract_dataframe


def clean_df(df):
    """
    Takes pandas DataFrame and performs transformations.
    Transformation 1: Removes "na" values
    Transformation 2: Drops duplicate rows
    Transformation 3: Adds country code to phone numbers
    Transformation 4: Creates atomic location
    :param df: Pandas DataFrame object
    :return df: Clean pandas Dataframe
    """
    df = df.query("bedroom != 'na' & bathroom != 'na'")
    df = df.drop_duplicates()
    df['user_phone'] = df['user_phone'].apply(lambda x: '+256' + str(x))
    df['location'] = df['location'].apply(lambda x: x.split('/')[0].strip())

    return df
