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

def read_data(data_file, header_file, filter=None):
  fields = read_header(header_file);
  with open(data_file) as f:
    reader = csv.DictReader(f, fieldnames=fields, dialect='excel-tab')
    rows = []
    for data in reader:
      if filter and filter(data):
        row = {}
        for field in fields:
          row[field] = parse(data[field])
        print(row)
        rows.append(row)
    return rows

def data_dir():
  here = os.path.abspath(os.path.dirname(__file__))
  return os.path.join(here, '..', 'data')
