import pandas as pd

from .config import default_config


def read_fields(fields_file):
    with open(fields_file, encoding='utf-8') as f:
        fields = [line.strip() for line in f.readlines()]
        return fields


def read_data(data_file, fields_file, delimiter='\t', filter=None, **kwargs):
    fields = read_fields(fields_file)
    df = pd.read_csv(data_file, names=fields, header=None,
                     delimiter=delimiter, encoding=encoding, encoding_errors='ignore', **kwargs)
    if filter:
        return filter(df)
    return df


def load(table, config=default_config, filter=None, **kwargs):
    data_file = config[f'{table}data']
    fields_file = config[f'{table}fields']
    df = read_data(data_file, fields_file, filter=filter, **kwargs)
    return df
