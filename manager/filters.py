def is_bigger_than(min_population):
	return lambda city: city['population'] >= min_population

def is_alternatename_for(geonameid):
	return lambda alternatename: alternatename['geonameid'] == geonameid

def is_alternatename_for_any_of(geonameids):
	return lambda alternatename: alternatename['geonameid'] in geonameids

def is_relevant_alternatename(alternatename):
	return (
		alternatename['isShortName'] != 1 and 
		alternatename['isHistoric'] != 1 and
		alternatename['isColloquial'] != 1 and
		alternatename['isolanguage'] != '' and
		alternatename['isolanguage'] != 'link'
	)

def is_relevant_alternatename_for_any_of(geonameids):
	return lambda alternatename: (
		is_relevant_alternatename(alternatename) and
		is_alternatename_for_any_of(geonameids)
	)

def is_local_alternatename(geonameid, language):
		return lambda alternatename: (
			alternatename['geonameid'] == geonameid and
			alternatename['isolanguage'] == language
		)

