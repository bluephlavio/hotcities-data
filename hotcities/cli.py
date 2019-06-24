import argparse
import os

from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd


from .config import read_config, default_config
from .readers import load
from .filters import cities_filter, countries_filter, alternatenames_filter
from .mergers import merge

def extract(args):
	config = read_config(args.config_file, section=args.section) if args.config_file else default_config
	cities = load('cities', filter=cities_filter(min_population=args.min_population), config=config)
	countries = load('countries', filter=countries_filter(), config=config)
	alternatenames = load('alternatenames', filter=alternatenames_filter(), config=config)
	data = merge(cities, countries, alternatenames)
	if args.out_file:
		data.to_csv(args.out_file, index=False)
	else:
		print(data.to_csv(index=False))


def upload(args):
	datafile = args.datafile
	env_file = args.env_file
	load_dotenv(dotenv_path=env_file)
	print('Secret keys loaded.')
	db_connection = os.getenv('MONGODB_CONNECTION')
	client = MongoClient(db_connection)
	print('Connected to database.')
	db_name = os.getenv('MONGODB_NAME')
	db = client[db_name]
	cities = db['cities']
	docs = pd.read_csv(datafile)
	updated = 0
	uploaded = 0
	total = 0
	for doc in docs:
		geonameid = doc['geonameid']
		name = doc['name']
		old = cities.find_one({ 'geonameid': geonameid })
		if old:
			print(f'Updating {name} ({total})...')
			updated += 1
		else:
			print(f'Uploading {name} ({total})...')
			uploaded += 1
		total += 1
		cities.find_one_and_replace({ 'geonameid': geonameid }, doc, upsert=True)
	print(f'{uploaded} cities uploaded and {updated} updated.')
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
	upload_subparser.add_argument('--env-file', default='.env.dev')
	upload_subparser.set_defaults(func=upload)

	args = parser.parse_args()
	args.func(args)

if __name__ == '__main__':
	main()