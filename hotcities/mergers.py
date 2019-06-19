import pandas as pd

pd.options.mode.chained_assignment = None

merged_data_fields = [
    'geonameid',
    'name',
    'localname',
    'population',
    'countryname',
    'countrycode',
    'lat',
    'lng',
]


def merge(cities, countries, alternatenames):
    cities = cities[['geonameid',
                     'name', 'country code', 'population', 'latitude', 'longitude']]
    cities.rename(lambda name: str(name).replace(
        ' ', '').lower(), axis='columns', inplace=True)
    cities.rename(columns={'latitude': 'lat',
                           'longitude': 'lng'}, inplace=True)
    countries = countries[['ISO', 'Country', 'Languages']]
    countries.rename(lambda name: str(name).replace(
        ' ', '').lower(), axis='columns', inplace=True)
    countries.rename(
        columns={'iso': 'countrycode', 'country': 'countryname', 'languages': 'lang'}, inplace=True)
    countries['lang'] = countries['lang'].apply(
        lambda langs: str(langs).split(',')[0][:2])
    alternatenames = alternatenames[(alternatenames['isShortName'] !=
                                     1) & (alternatenames['isColloquial'] != 1) & (alternatenames['isHistoric'] != 1)]
    alternatenames = alternatenames[[
        'geonameid', 'alternate name', 'isolanguage']]
    alternatenames.rename(lambda name: str(name).replace(
        ' ', '').lower(), axis='columns', inplace=True)
    alternatenames.rename(
        columns={'isolanguage': 'lang'}, inplace=True)
    merged_data = pd.merge(cities, countries, on='countrycode')
    merged_data = pd.merge(merged_data,
                           alternatenames, on=['geonameid', 'lang'])
    merged_data = merged_data.groupby(by=[
        'geonameid',
        'name',
        'population',
        'countryname',
        'countrycode',
        'lat',
        'lng',
    ], as_index=False).agg(
        {'alternatename': lambda series: series.tolist()})
    merged_data['localname'] = merged_data['alternatename'].apply(
        lambda x: x[0])
    merged_data = merged_data[merged_data_fields]
    return merged_data
