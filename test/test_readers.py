import pytest
import pandas as pd

from hotcities.readers import read_fields, read_data


def test_read_fields(fields_file):
    fields = read_fields(fields_file)
    for i, field in enumerate(fields):
        assert field == list(['a', 'b', 'c'])[i]


def test_read_data(data_file, fields_file):
    df = read_data(data_file, fields_file)
    for i, row in df.iterrows():
        assert row['a'] == 3 * i + 1
        assert row['b'] == 3 * i + 2
        assert row['c'] == 3 * i + 3

