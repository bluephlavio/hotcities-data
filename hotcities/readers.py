import csv

from .parsers import parse
from .config import default_config

def read_fields(filename):
  with open(filename, encoding='utf-8') as f:
    return [line.strip() for line in f.readlines()]

def read_data(data_file, fields_file=None, dialect='excel-tab', where=lambda x: True, hook=None):
  fields = read_fields(fields_file) if fields_file else None
  with open(data_file, encoding='utf-8') as f:
    reader = csv.DictReader(f, fieldnames=fields, dialect=dialect, quoting=csv.QUOTE_NONE)
    rows = []
    i = 0
    for line in reader:
      row = {}
      for field in reader.fieldnames:
        row[field] = parse(line[field])
      if where and where(row):
        rows.append(row)
        if hook:
          hook(row, i)
        i += 1
    return rows

def load(table, where=lambda x: True, hook=None, config=default_config):
  data_file = config[f'{table}data']
  fields_file = config[f'{table}fields']
  return read_data(data_file, fields_file, where=where, hook=hook)