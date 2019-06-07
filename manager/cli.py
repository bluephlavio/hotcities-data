import argparse

from .merge import merge_city_data
from .helpers import load

parser = argparse.ArgumentParser(
	description='hotcities-data manager cli.'
)
parser.add_argument('--minpopulation',
	default=1000000
)

def main():
	args = parser.parse_args()
	print('hello')
	print(args.minpopulation)

if __name__ == '__main__':
	main()