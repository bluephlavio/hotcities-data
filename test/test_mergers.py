import pytest

from hotcities.readers import load
from hotcities.filters import cities_filter, countries_filter, alternatenames_filter
from hotcities.mergers import merge


@pytest.fixture
def data(config):
    cities = load('cities', filter=cities_filter(
        min_population=100000), config=config)
    countries = load('countries', filter=countries_filter(), config=config)
    alternatenames = load(
        'alternatenames', filter=alternatenames_filter(), config=config)
    return cities, countries, alternatenames


def test_merge(data):
    cities, countries, alternatenames = data
    merged_data = merge(cities, countries, alternatenames)
    for i, row in merged_data.iterrows():
        assert row['countrycode'] == 'AE'
        assert row['countryname'] == 'United Arab Emirates'
