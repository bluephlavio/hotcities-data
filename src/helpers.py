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

def read_data(data_file, header_file, filter=None):
  fields = read_header(header_file);
  with open(data_file, encoding='utf-8') as f:
    reader = csv.DictReader(f, fieldnames=fields, dialect='excel-tab')
    rows = []
    for data in reader:
      row = {}
      for field in fields:
        row[field] = parse(data[field])
      if filter and filter(row):
        rows.append(row)
    return rows

def data_dir():
  here = os.path.abspath(os.path.dirname(__file__))
  return os.path.join(here, '..', 'data')
