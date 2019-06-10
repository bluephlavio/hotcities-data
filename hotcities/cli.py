import argparse
import sys
import os
import csv
from pymongo import MongoClient
from dotenv import load_dotenv

from .config import read_config, default_config
from .mergers import merge_cities_data
from .filters import is_bigger_than, is_relevant_alternatename_for_any_of
from .readers import load, read_data
from .loggers import log_merging_cities, log_loading_cities, log_loading_countries, log_loading_alternatenames


def extract(args):
	config = read_config(args.config_file, section=args.section) if args.config_file else default_config
	cities = load('cities', where=is_bigger_than(args.min_population), hook=log_loading_cities, config=config)
	geonameids = list(map(lambda city: city['geonameid'], cities))
	countries = load('countries', hook=log_loading_countries, config=config)
	alternatenames = load('alternatenames', where=is_relevant_alternatename_for_any_of(geonameids), hook=log_loading_alternatenames, config=config)
	data, fields = merge_cities_data(cities, countries, alternatenames, hook=log_merging_cities)
	if args.out_file:
		with open(args.out_file, 'w', newline='', encoding='utf-8') as f:
			writer = csv.DictWriter(f, fieldnames=fields)
			writer.writeheader()
			for city in data:
				writer.writerow(city)
	else:
		for city in data:
			values_list = list(map(lambda field: str(city[field]), fields))
			print(','.join(values_list))


def upload(args):
	datafile = args.datafile
	load_dotenv()
	connection = os.getenv('MONGODB_CONNECTION')
	client = MongoClient(connection)
	print('Connected to database...')
	db = client['hotcities-dev']
	cities = db['cities']
	docs = read_data(datafile, dialect='excel')
	updated = 0
	uploaded = 0
	for doc in docs:
		geonameid = doc['geonameid']
		name = doc['name']
		old = cities.find_one({ 'geonameid': geonameid })
		if old:
			print(f'Updating {name}...')
			updated += 1
		else:
			print(f'Uploading {name}...')
			uploaded += 1
		cities.find_one_and_replace({ 'geonameid': geonameid }, doc, upsert=True)
	print(f'{uploaded} cities uploaded and {updated} updated')
	client.close()
	print('Database connection closed.')

def main():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers()

	extract_subparser = subparsers.add_parser('extract')
	extract_subparser.add_argument('--min-population', type=int, default=10000000)
	extract_subparser.add_argument('--out-file', default=None)
	extract_subparser.add_argument('--config-file', default=None)
	extract_subparser.add_argument('--section', default='DEFAULT')
	extract_subparser.set_defaults(func=extract)

	upload_subparser = subparsers.add_parser('upload')
	upload_subparser.add_argument('datafile')
	upload_subparser.set_defaults(func=upload)

	args = parser.parse_args()
	args.func(args)

if __name__ == '__main__':
	main()