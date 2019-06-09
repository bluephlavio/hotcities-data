import pytest

from manager.readers import read_fields, read_data

def test_read_fields(fields_file):
  fields = read_fields(fields_file)
  for i, field in enumerate(fields):
    assert field == list(['a', 'b', 'c'])[i]

def test_read_data(data_file, fields_file):
  rows = read_data(data_file, fields_file)
  for i, row in enumerate(rows):
    assert row['a'] == 3 * i + 1
    assert row['b'] == 3 * i + 2
    assert row['c'] == 3 * i + 3

def test_read_filtered_data(data_file, fields_file):
  rows = read_data(data_file, fields_file, where=lambda row: row['a'] != 1)
  assert len(rows) == 2
  for i, row in enumerate(rows):
    assert row['a'] == 3 * i + 4
    assert row['b'] == 3 * i + 5
    assert row['c'] == 3 * i + 6