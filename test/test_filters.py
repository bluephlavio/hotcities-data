import pytest
import os

from manager.filters import is_bigger_than

@pytest.fixture
def cities():
	return [
		{ 'population': 1 },
		{ 'population': 10, 'name': 'Sharjah', 'localname': None },
		{ 'population': 100, 'geonameid': 0 }
	]

def test_is_bigger_than(cities):
	filtered_cities = list(filter(is_bigger_than(10), cities))
	assert len(filtered_cities) == 2
	assert filtered_cities[1]['geonameid'] == 0
