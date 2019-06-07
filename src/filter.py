from .helpers import read_data, data_dir

def filter_cities_by_population(min_population, cities_file, header_file):
	cities = read_data(cities_file, header_file, filter=lambda city: city['population'] >= min_population)
	return cities

def filter_alternate_names_for_cities(cities, alternate_names_file, header_file):
	geonameids = list(map(lambda city: city['geonameid'], cities))
	filter = lambda alternate_name: alternate_name['geonameid'] in geonameids
	alternate_names = read_data(alternate_names_file, header_file, filter=filter)
	return alternate_names
