from typing import List
from unicodedata import name

import pandas as pd


def add_file_name_to_columns(df, file_name):
    df.drop(['Name', 'Symbol'], axis=1, inplace=True)
    df.columns = [
        f'{file_name}_{col}'.lower() if col != 'Date' else 'date'
        for col in df.columns
    ]
    return df


def left_join_df_by_date(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df1 = df1.set_index('date')
    df2 = df2.set_index('date')
    df = df1.join(df2, how='left')
    df.reset_index(inplace=True)
    return df


def create_dataframes(files: List[str]) -> list:
    df = pd.DataFrame()
    for i, file in enumerate(files):
        _df = pd.read_csv(f'data/external/{file}.csv', parse_dates=['Date'])
        _df = add_file_name_to_columns(_df, file)
        print(f'{file} shape: {_df.shape}')
        if i:
            df = left_join_df_by_date(df, _df)
        else:
            df = _df
    return df


if __name__ == '__main__':
    files = ['bitcoin', 'ethereum', 'cardano']
    df = create_dataframes(files)
    df.to_csv('data/processed/dataset.csv', index=False)