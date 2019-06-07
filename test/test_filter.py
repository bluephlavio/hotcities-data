import pytest
import os

from src.filter import filter_cities_by_population, filter_alternate_names_for_cities

def test_filter_cities_by_population(test_data_files):
	cities = filter_cities_by_population(100000, data_files=test_data_files)
	assert len(cities) == 1
	assert cities[0]['geonameid'] == 291074

def test_filter_alternate_names_by_cities(test_data_files):
	cities = filter_cities_by_population(100000, data_files=test_data_files)
	alternate_names = filter_alternate_names_for_cities(cities, data_files=test_data_files)
	assert len(alternate_names) == 12