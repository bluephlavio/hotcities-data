import csv
import os

def parse(value):
  try:
    return int(value)
  except ValueError:
    try:
      return float(value)
    except ValueError:
      return value

def read_header(filename):
  with open(filename) as f:
    return [line.strip() for line in f.readlines()]

def read_data(data_file, header_file):
  fields = read_header(header_file);
  with open(data_file) as f:
    reader = csv.DictReader(f, fieldnames=fields, dialect='excel-tab')
    data = list(reader)
    for row in data:
      for field in fields:
        row[field] = parse(row[field])
    return data

def data_dir():
  here = os.path.abspath(os.path.dirname(__file__))
  return os.path.join(here, '..', 'data')

def load_cities():
  cities_file = os.path.join(data_dir(), 'cities15000.txt')
  header_file = os.path.join(data_dir(), 'citiesHeader.txt')
  cities = read_data(cities_file, header_file)
  return cities