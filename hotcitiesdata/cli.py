import argparse
import sys
import csv

from .config import read_config, default_config
from .mergers import merge_cities_data
from .filters import is_bigger_than, is_relevant_alternatename_for_any_of
from .readers import load

def extract(args):
	config = read_config(args.config_file) if args.config_file else default_config
	cities = load('cities', where=is_bigger_than(args.min_population), config=config)
	geonameids = list(map(lambda city: city['geonameid'], cities))
	countries = load('countries', config=config)
	alternatenames = load('alternatenames', where=is_relevant_alternatename_for_any_of(geonameids), config=config)
	data, fields = merge_cities_data(cities, countries, alternatenames)
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

def main():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers()

	extract_subparser = subparsers.add_parser('extract')
	extract_subparser.add_argument('--min-population', type=int, default=10000000)
	extract_subparser.add_argument('--out-file', default=None)
	extract_subparser.add_argument('--config-file', default=None)
	extract_subparser.set_defaults(func=extract)

	args = parser.parse_args()
	args.func(args)

if __name__ == '__main__':
	main()