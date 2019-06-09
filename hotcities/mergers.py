from collections import OrderedDict

from .filters import is_local_alternatename

merged_cities_data_fields = [
	'geonameid',
	'name',
	'localname',
	'population',
	'countryname',
	'countrycode',
	'timezone',
	'lng',
	'lat',
	'lang'
]

def merge_city_data(city, countries, alternatenames):
	geonameid = city['geonameid']
	name = city['name']
	countrycode = city['country code']
	timezone = city['timezone']
	population = city['population']
	lng = city['longitude']
	lat = city['latitude']
	country, = (country for country in countries if country['ISO'] == countrycode)
	languages = country['Languages'].split(',')
	lang = languages[0][:2]
	localnames = list(filter(is_local_alternatename(geonameid, lang), alternatenames))
	localname = None
	if len(localnames) > 0:
		localname = localnames[0]['alternate name']
	countryname = country['Country']
	merged_data = OrderedDict()
	merged_data['geonameid'] = geonameid
	merged_data['name'] = name
	merged_data['localname'] = localname
	merged_data['population'] = population
	merged_data['countryname'] = countryname
	merged_data['countrycode'] = countrycode
	merged_data['timezone'] = timezone
	merged_data['lng'] = lng
	merged_data['lat'] = lat
	merged_data['lang'] = lang
	return merged_data

def merge_cities_data(cities, countries, alternatenames):
	merged_data = []
	for city in cities:
		merged_data.append(merge_city_data(city, countries, alternatenames))
	return merged_data, merged_cities_data_fields