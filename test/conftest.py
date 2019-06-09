import pytest
import os.path

from manager.config import read_config

@pytest.fixture(scope='session')
def res_dir():
  here = os.path.abspath(os.path.dirname(__file__))
  return os.path.join(here, 'res' + os.path.sep)

@pytest.fixture(scope='session')
def fields_file(res_dir):
  return os.path.join(res_dir, 'fields.txt')

@pytest.fixture(scope='session')
def data_file(res_dir):
  return os.path.join(res_dir, 'data.txt')

@pytest.fixture
def config(res_dir):
  return read_config(os.path.join(res_dir, 'config.test.ini'))
