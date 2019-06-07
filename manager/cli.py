import argparse
import sys
import csv

from .merge import merge_city_data, merged_data_fields
from .filter import filter_cities_by_population

def extract(args):
	cities_table = filter_cities_by_population(args.min_population)
	cities = list(map(merge_city_data, cities_table))
	fieldnames = merged_data_fields()
	if args.out_file:
		with open(args.out_file, 'w', newline='', encoding='utf-8') as f:
			writer = csv.DictWriter(f, fieldnames=fieldnames)
			writer.writeheader()
			for city in cities:
				writer.writerow(city)
	else:
		print(','.join(fieldnames))
		for city in cities:
			values_list = list(map(lambda field: str(city[field]), fieldnames))
			print(','.join(values_list))

def main():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers()

	extract_subparser = subparsers.add_parser('extract')
	extract_subparser.add_argument('--min-population', type=int, default=10000000)
	extract_subparser.add_argument('--out-file', default=None)
	extract_subparser.set_defaults(func=extract)

	args = parser.parse_args()
	args.func(args)

if __name__ == '__main__':
	main()