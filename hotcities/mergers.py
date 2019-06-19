import pandas as pd

pd.options.mode.chained_assignment = None


def merge(cities, countries, alternatenames):
    cities = cities[['geonameid',
                     'name', 'country code', 'population']]
    cities.rename(lambda name: str(name).replace(
        ' ', '').lower(), axis='columns', inplace=True)
    countries = countries[['ISO', 'Country', 'Languages']]
    countries.rename(lambda name: str(name).replace(
        ' ', '').lower(), axis='columns', inplace=True)
    countries.rename(
        columns={'iso': 'countrycode', 'country': 'countryname', 'languages': 'lang'}, inplace=True)
    countries['lang'] = countries['lang'].apply(
        lambda langs: str(langs).split(',')[0][:2])
    alternatenames = alternatenames[[
        'geonameid', 'alternate name', 'isolanguage']]
    alternatenames.rename(lambda name: str(name).replace(
        ' ', '').lower(), axis='columns', inplace=True)
    alternatenames.rename(
        columns={'isolanguage': 'lang'}, inplace=True)
    merged_data = cities.merge(countries, on='countrycode')
    merged_data = merged_data.merge(
        alternatenames, how='inner', on=['geonameid', 'lang'])
    return merged_data
