import pytest

from hotcities.readers import load
from hotcities.mergers import merge


@pytest.fixture
def data(config):
    cities = load('cities', config=config)
    countries = load('countries', config=config)
    alternatenames = load('alternatenames', config=config)
    return cities, countries, alternatenames


def test_merge(data):
    cities, countries, alternatenames = data
    merged_data = merge(cities, countries, alternatenames)
    for i, row in merged_data.iterrows():
        assert row['countrycode'] == 'AE'
        assert row['countryname'] == 'United Arab Emirates'
