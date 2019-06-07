import pytest

import os.path

@pytest.fixture(scope='session')
def res_dir():
  here = os.path.abspath(os.path.dirname(__file__))
  return os.path.join(here, 'res' + os.path.sep)

@pytest.fixture(scope='session')
def header_file(res_dir):
  return os.path.join(res_dir, 'header.txt')

@pytest.fixture(scope='session')
def data_file(res_dir):
  return os.path.join(res_dir, 'data.txt')

@pytest.fixture
def cities_file(res_dir):
	return os.path.join(res_dir, 'cities.txt')

@pytest.fixture
def cities_header_file(res_dir):
	return os.path.join(res_dir, 'citiesHeader.txt')

@pytest.fixture
def alternate_names_file(res_dir):
	return os.path.join(res_dir, 'alternateNames.txt')

@pytest.fixture
def alternate_names_header_file(res_dir):
	return os.path.join(res_dir, 'alternateNamesHeader.txt')
