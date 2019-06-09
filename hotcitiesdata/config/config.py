import os
import configparser

here = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(here, '..', '..', 'data')

keys = [
	'citiesdata',
	'citiesfields',
	'countriesdata',
	'countriesfields',
	'alternatenamesdata',
	'alternatenamesfields'
]

defaults = { key: os.path.join(data_dir, key) for key in keys }

default_config_file = os.path.join(here, 'config.ini')

def read_config(config_file, section='DEFAULT'):
	config_file_dir = os.path.dirname(os.path.abspath(config_file))
	parser = configparser.ConfigParser()
	parser.read(config_file)
	config = parser[section]
	for key in keys:
		config[key] = os.path.join(config_file_dir, config.get(key, defaults[key]))
	return config

default_config = read_config(default_config_file)