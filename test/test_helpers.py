import pytest

from manager.helpers import parse, read_header, read_data

@pytest.fixture(params=[
  ('a', 'a'),
  ('1', 1),
  ('1.0', 1.0)
])
def parse_data(request):
  return request.param

def test_parse(parse_data):
  param, result = parse_data
  assert parse(param) == result

def test_read_header(header_file):
  fields = read_header(header_file)
  for i, field in enumerate(fields):
    assert field == list(['a', 'b', 'c'])[i]

def test_read_data(data_file, header_file):
  rows = read_data(data_file, header_file)
  for i, row in enumerate(rows):
    assert row['a'] == 3 * i + 1
    assert row['b'] == 3 * i + 2
    assert row['c'] == 3 * i + 3

def test_read_filtered_data(data_file, header_file):
  rows = read_data(data_file, header_file, lambda row: row['a'] != 1)
  assert len(rows) == 2
  for i, row in enumerate(rows):
    assert row['a'] == 3 * i + 4
    assert row['b'] == 3 * i + 5
    assert row['c'] == 3 * i + 6