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
def test_data_files(res_dir):
  return {
    'cities': (os.path.join(res_dir, 'cities.txt'), os.path.join(res_dir, 'citiesHeader.txt')),
    'countries': (os.path.join(res_dir, 'countries.txt'), os.path.join(res_dir, 'countriesHeader.txt')),
    'alternate_names': (os.path.join(res_dir, 'alternateNames.txt'), os.path.join(res_dir, 'alternateNamesHeader.txt')),
    'languages': (os.path.join(res_dir, 'languages.txt'), os.path.join(res_dir, 'languagesHeader.txt')),
  }
