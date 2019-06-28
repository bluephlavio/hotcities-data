import pandas as pd

# pd.options.mode.chained_assignment = None


def merge(cities, countries, alternatenames):
    cities_with_lang = pd.merge(cities, countries, on='countrycode')
    df = pd.merge(
        cities_with_lang, alternatenames, how='left', on=['geonameid', 'lang'])
    df.rename(
        columns={'alternatename': 'localname'}, inplace=True)
    return df
