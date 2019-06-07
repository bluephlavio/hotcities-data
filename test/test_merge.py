from manager.helpers import load
from manager.merge import merge_city_data

def test_merge_city_data(test_data_files):
	cities = load('cities', data_files=test_data_files)
	for city in cities:
		merged_data = merge_city_data(city, data_files=test_data_files)
		assert merged_data['countrycode'] == 'AE'
		assert merged_data['lang'] == 'ar'