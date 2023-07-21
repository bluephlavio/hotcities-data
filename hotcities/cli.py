import os
import click
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd

from .config import read_config, default_config
from .readers import load
from .filters import cities_filter, countries_filter, alternatenames_filter
from .mergers import merge, merged_data_dtypes
from .google import Google
from .unsplash import Unsplash


@click.group()
@click.option(
    "--config-file",
    "-c",
    type=click.Path(exists=True),
    help="Path to the configuration file.",
)
@click.option(
    "--section",
    "-s",
    default="DEFAULT",
    help="Section of the configuration file to use.",
)
@click.pass_context
def cli(ctx, config_file, section):
    ctx.ensure_object(dict)
    ctx.obj["config"] = (
        read_config(
            config_file, section=section) if config_file else default_config
    )


@cli.command()
@click.option(
    "--min-population",
    type=int,
    default=0,
    help="Minimum population for cities to include.",
)
@click.option("--out-file", "-o", type=click.Path(), help="Path to the output file.")
@click.pass_context
def extract(ctx, min_population, out_file):
    click.echo("Reading cities data...")
    cities = load(
        "cities",
        filter=cities_filter(min_population=min_population),
        config=ctx.obj["config"],
    )
    click.echo(cities)
    click.echo("Reading coutries data...")
    countries = load("countries", filter=countries_filter(),
                     config=ctx.obj["config"])
    click.echo(countries)
    alternatenames = load(
        "alternatenames",
        filter=alternatenames_filter(),
        config=ctx.obj["config"],
        low_memory=False,
    )
    click.echo("Reading alternate names data...")
    click.echo(alternatenames)
    click.echo("Merging data...")
    data = merge(cities, countries, alternatenames)
    click.echo(data)
    if out_file:
        data.to_csv(out_file, index=False)
        click.echo(f"Data saved to {out_file}")
    else:
        click.echo(data.to_csv(index=False))

# @click.command()
# @click.argument("data_file", type=click.Path(exists=True))
# @click.argument("env_file", type=click.Path(exists=True))
# def upload(data_file, env_file):
#     load_dotenv(dotenv_path=env_file)
#     click.echo("Secret keys loaded.")
#     db_connection = os.getenv("MONGODB_CONNECTION")
#     db_name = os.getenv("MONGODB_NAME")
#     client = MongoClient(db_connection)
#     db = client[db_name]
#     click.echo("Connected to database.")
#     data = pd.read_csv(data_file, dtype=merged_data_dtypes)
#     data = data.where(data.notnull(), None)
#     cities = data.to_dict("records")
#     for i, city in enumerate(cities):
#         geonameid = city["geonameid"]
#         name = str(city["name"]) if city["name"] is not None else ""
#         db["cities"].find_one_and_replace(
#             {"geonameid": geonameid}, city, upsert=True)
#         click.echo(f"Uploading {name} to db ({i}/{len(cities)})...")
#     click.echo(f"All {len(cities)} cities uploaded.")
#     client.close()
#     click.echo("Database connection closed.")
