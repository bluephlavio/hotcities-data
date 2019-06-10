def log_loading_table(table, field):
	def log(row, i):
		print(f'Loading {table} ({i+1}): reading {row[field]}...')
	return log

log_loading_cities = log_loading_table('cities', 'name')
log_loading_countries = log_loading_table('countries', 'Country')
log_loading_alternatenames = log_loading_table('alternatenames', 'alternate name')

def log_merging_cities(city, i, cities):
	name = city['name']
	print(f'Merging data ({i+1} of {len(cities)}): processing {name}...')