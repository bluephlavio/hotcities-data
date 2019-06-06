import csv

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
