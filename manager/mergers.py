from .filters import is_local_alternatename

merged_cities_data_fields = {
	'geonameid',
	'name',
	'localname',
	'countryname',
	'countrycode',
	'timezone',
	'population',
	'lang',
	'lng',
	'lat'
}

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
		localname = localnames[0]
	countryname = country['Country']
	return {
		'geonameid': geonameid,
		'name': name,
		'localname': localname,
		'countryname': countryname,
		'countrycode': countrycode,
		'timezone': timezone,
		'population': population,
		'lang': lang,
		'lng': lng,
		'lat': lat
	}

def merge_cities_data(cities, countries, alternatenames):
	merged_data = []
	for city in cities:
		merged_data.append(merge_city_data(city, countries, alternatenames))
	return merged_data, merged_cities_data_fields