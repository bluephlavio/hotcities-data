import os
import configparser

here = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(here, '..', '..', 'data')
default_config_file = os.path.join(here, 'config.ini')

def parse_file_path_value(file_path, config_file_path):
	config_file_dir = os.path.dirname(os.path.abspath(config_file_path))
	return os.path.join(os.path.abspath(config_file_dir), file_path)

entries = {
	'citiesdata': (os.path.join(data_dir, 'cities.data.txt'), parse_file_path_value),
	'citiesfields': (os.path.join(data_dir, 'cities.fileds.txt'), parse_file_path_value),
	'countriesdata': (os.path.join(data_dir, 'countries.data.txt'), parse_file_path_value),
	'countriesfields': (os.path.join(data_dir, 'countries.fields.txt'), parse_file_path_value),
	'alternatenamesdata': (os.path.join(data_dir, 'alternatenames.data.txt'), parse_file_path_value),
	'alternatenamesfields': (os.path.join(data_dir, 'alternatenames.fields.txt'), parse_file_path_value)
}

def read_config(config_file, section='DEFAULT'):
	cp = configparser.ConfigParser()
	cp.read(config_file)
	config = cp[section]
	for key in entries.keys():
		default, parser = entries[key]
		value = config.get(key, default)
		if parser:
			value = parser(value, config_file)
		config[key] = value
	return config

default_config = read_config(default_config_file)