import csv

def read_header(filename):
  with open(filename) as f:
    return [line.strip() for line in f.readlines()]

def read_data(data_file, header_file):
  header = read_header(header_file);
  with open(data_file) as f:
    reader = csv.DictReader(f, fieldnames=header, dialect='excel-tab')
    return [row for row in reader]