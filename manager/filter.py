from .helpers import load, default_data_files

def filter_cities_by_population(min_population, data_files=default_data_files()):
	cities = load('cities', data_files=data_files, where=lambda city: city['population'] >= min_population)
	return cities

def filter_alternate_names_for_cities(cities, data_files=default_data_files()):
	geonameids = list(map(lambda city: city['geonameid'], cities))
	def is_ok(name):
		return (
			name['isShortName'] != 1 and 
			name['isHistoric'] != 1 and
			name['isColloquial'] != 1 and
			name['isolanguage'] != '' and
			name['isolanguage'] != 'link' and
			name['geonameid'] in geonameids
		)
	alternate_names = load('alternate_names', data_files=data_files, where=is_ok)
	return alternate_names

