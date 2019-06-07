from .helpers import load, default_data_files

def merge_city_data(city, alternate_names, data_files=default_data_files()):
	geonameid = city['geonameid']
	name = city['name']
	countrycode = city['country code']
	timezone = city['timezone']
	population = city['population']
	lng = city['longitude']
	lat = city['latitude']
	country, = load('countries', data_files=data_files, where=lambda country: country['ISO'] == countrycode)
	languages = country['Languages'].split(',')
	language = languages[0][:2]
	def is_local_name(name):
		return name['geonameid'] == geonameid and name['isolanguage'] == language
	local_names = list(filter(is_local_name, alternate_names))
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
		'lang': language,
		'lng': lng,
		'lat': lat
	}

def merged_data_fields():
	return [
		'geonameid',
		'name',
		'localname',
		'country',
		'countrycode',
		'timezone',
		'population',
		'lang',
		'lng',
		'lat'
	]