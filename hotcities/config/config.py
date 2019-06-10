import os
import configparser

here = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(here, '..', '..', 'data')
default_config_file = os.path.join(here, 'config.ini')

def parse_file_path(filename, config_file):
	config_file_dir = os.path.dirname(os.path.abspath(config_file))
	return os.path.join(os.path.abspath(config_file_dir), filename)

entries = {
	'citiesdata': (parse_file_path, os.path.join(data_dir, 'cities.data.txt')),
	'citiesfields': (parse_file_path, os.path.join(data_dir, 'cities.fileds.txt')),
	'countriesdata': (parse_file_path, os.path.join(data_dir, 'coutries.data.txt')),
	'countriesfields': (parse_file_path, os.path.join(data_dir, 'countries.fields.txt')),
	'alternatenamesdata': (parse_file_path, os.path.join(data_dir, 'alternatenames.data.txt')),
	'alternatenamesfields': (parse_file_path, os.path.join(data_dir, 'alternatenames.fields.txt'))
}

def read_config(config_file, section='DEFAULT'):
	parser = configparser.ConfigParser()
	parser.read(config_file)
	config = parser[section]
	for key in entries.keys():
		parser, default = entries[key]
		value = config.get(key, default)
		if parser:
			value = parser(value, config_file)
		config[key] = value
	return config

default_config = read_config(default_config_file)