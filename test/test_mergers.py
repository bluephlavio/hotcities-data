import pytest

from manager.readers import load
from manager.mergers import merge_city_data

@pytest.fixture
def data(config):
	cities = load('cities', config=config)
	countries = load('countries', config=config)
	alternatenames = load('alternatenames', config=config)
	return cities, countries, alternatenames

def test_merge_city_data(data):
	cities, countries, alternatenames = data
	for city in cities:
		merged_data = merge_city_data(city, countries, alternatenames)
		assert merged_data['countrycode'] == 'AE'
		assert merged_data['lang'] == 'ar'