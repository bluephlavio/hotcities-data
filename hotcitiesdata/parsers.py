def numberify(value):
  try:
    return int(value)
  except:
    return float(value)

def parse(value):
	try:
		return numberify(value)
	except:
		return value
