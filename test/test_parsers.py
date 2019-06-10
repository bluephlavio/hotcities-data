import pytest

from hotcities.parsers import parse

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
