from .helpers import load, default_data_files

def merge_city_data(city, data_files=default_data_files()):
	geonameid = city['geonameid']
	name = city['name']
	countrycode = city['countrycode']
	timezone = city['timezone']
	population = city['population']
	lng = city['lng']
	lat = city['lat']
	country, = load('countries', data_files=data_files, where=lambda country: country['ISO'] == countrycode)
	languages = country['Languages'].split(',')
	language = languages[0]
	def is_local_name(name):
		return name['geonameid'] == geonameid and name['isolanguage'] == language
	local_names = load('alternate_names', data_files=test_data_files, where=is_local_name)
	local_name = None
	if len(local_names) > 0:
		local_name = local_names[0]
	return {
		'geonameid': geonameid,
		'name': name,
		'localname': local_name,
		'country': country['Country'],
		'countrycode': countrycode,
		'timezone': timezone,
		'population': population,
		'lang': language['ISO 639-3'],
		'lng': lng,
		'lat': lat
	}