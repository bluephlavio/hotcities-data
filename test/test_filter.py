import pytest
import os

from src.filter import filter_cities_by_population, filter_alternate_names_for_cities

def test_filter_cities_by_population(cities_file, cities_header_file):
	cities = filter_cities_by_population(100000, cities_file, cities_header_file)
	assert len(cities) == 1
	assert cities[0]['geonameid'] == 291074

def test_filter_alternate_names_by_cities(cities_file, cities_header_file, alternate_names_file, alternate_names_header_file):
	cities = filter_cities_by_population(100000, cities_file, cities_header_file)
	alternate_names = filter_alternate_names_for_cities(cities, alternate_names_file, alternate_names_header_file)
	assert len(alternate_names) == 19