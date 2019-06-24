import numpy as np
import pandas as pd

cities_fields = [
    'geonameid',
    'name',
    'countrycode',
    'population',
    'lat',
    'lng',
    'timezone'
]

countries_fields = [
    'countrycode',
    'countryname',
    'lang'
]

alternatenames_fields = [
    'geonameid',
    'lang',
    'alternatename'
]


def cities_filter(min_population=500000, columns=cities_fields):
    def filter(df):
        return df.loc[df['population'] >= min_population][columns]
    return filter


def filter_languages(languages):
    return languages.split(',')[0][:2] if pd.notnull(languages) else np.nan


def countries_filter(columns=countries_fields):
    def filter(df):
        df['lang'] = df['languages'].apply(filter_languages)
        return df[columns]
    return filter


def alternatenames_filter(columns=alternatenames_fields):
    def filter(df):
        newdf = df.loc[pd.notnull(df['lang']) & (df['lang'] != 'link') & pd.isnull(
            df['isshortname']) & pd.isnull(df['iscolloquial']) & pd.isnull(df['ishistoric'])]
        newdf = newdf[columns]
        newdf = newdf.groupby(['geonameid', 'lang']).agg(
            {'alternatename': lambda series: list(series)[0]})
        return newdf
    return filter
