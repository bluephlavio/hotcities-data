import numpy as np
import pandas as pd

# pd.options.mode.chained_assignment = None


def merge(cities, countries, alternatenames):
    cities_with_lang = pd.merge(cities, countries, on='countrycode')
    cities_with_localname = pd.merge(
        cities_with_lang, alternatenames, how='left', on=['geonameid', 'lang'])
    cities_with_localname.rename(
        columns={'alternatename': 'localname'}, inplace=True)
    return cities_with_localname
