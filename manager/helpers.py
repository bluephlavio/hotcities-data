import csv
import os

def parse(value):
  try:
    return int(value)
  except:
    try:
      return float(value)
    except:
      return value

def read_header(filename):
  with open(filename, encoding='utf-8') as f:
    return [line.strip() for line in f.readlines()]

def read_data(data_file, header_file, where=None):
  fields = read_header(header_file);
  with open(data_file, encoding='utf-8') as f:
    reader = csv.DictReader(f, fieldnames=fields, dialect='excel-tab')
    rows = []
    for data in reader:
      row = {}
      for field in fields:
        row[field] = parse(data[field])
      if where and where(row):
        rows.append(row)
    return rows

def data_dir():
  here = os.path.abspath(os.path.dirname(__file__))
  return os.path.join(here, '..', 'data')

def default_data_files():
  return {
    'cities': (os.path.join(data_dir(), 'cities.txt'), os.path.join(data_dir(), 'citiesHeader.txt')),
    'countries': (os.path.join(data_dir(), 'countries.txt'), os.path.join(data_dir(), 'countriesHeader.txt')),
    'alternate_names': (os.path.join(data_dir(), 'alternateNames.txt'), os.path.join(data_dir(), 'alternateNamesHeader.txt')),
    'languages': (os.path.join(data_dir(), 'languages.txt'), os.path.join(data_dir(), 'languagesHeader.txt')),
  }

def load(table, data_files=default_data_files(), where=None):
  data_file, header_file = data_files[table]
  return read_data(data_file, header_file, where=where)
