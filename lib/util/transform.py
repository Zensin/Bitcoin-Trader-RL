import numpy as np


def transform(df, columns=None, transform_fn=None):
    transformed_df = df.copy().fillna(method='bfill')

    if columns is None:
        transformed_df = transform_fn(transformed_df)
    else:
        for column in columns:
            transformed_df[column] = transform_fn(transformed_df[column])

    return transformed_df


def max_min_normalize(df, columns=None):
    return transform(df, columns, lambda t_df: (t_df - t_df.min()) / (t_df.max() - t_df.min()))


def difference(df, columns=None):
    return transform(df, columns, lambda t_df: t_df - t_df.shift(1))


def log_and_difference(df, columns=None):
    return transform(df, columns, lambda t_df: np.log(t_df) - np.log(t_df).shift(1))
