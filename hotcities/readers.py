import pandas as pd

from .config import default_config


def read_fields(fields_file):
    with open(fields_file, encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


def read_data(data_file, fields_file=None, delimiter='\t'):
    fields = read_fields(fields_file) if fields_file else None
    return pd.read_csv(data_file, names=fields, header=None if fields else 0, delimiter=delimiter)


def load(table, config=default_config):
    data_file = config[f'{table}data']
    fields_file = config[f'{table}fields']
    return read_data(data_file, fields_file)
