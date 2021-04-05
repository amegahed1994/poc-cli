import json
import logging

import click

from bq.datasets.compare import compare as bq_datasets_compare


@click.group()
@click.option(
    "--log-level",
    type=click.Choice(["ERROR", "WARNING", "INFO", "DEBUG"]),
    default="INFO",
    show_default=True,
    help="The desired logging level.",
)
def root(log_level):
    "Goal of this command-line interface is to centralize mmvt's scripts."
    logging.basicConfig(level=log_level)


@root.group()
def bq():
    "Scripts that performs QA on datasets post copy/migration."
    pass


@bq.group()
def datasets():
    pass


@datasets.command()
@click.option(
    "-f",
    "--from-json",
    required=True,
    type=click.File("r"),
    help="Path to the input json file.",
)
def compare(from_json):
    "Compares datasets lazily by checking their metadata."

    for dataset in json.load(from_json):
        src_dataset_id = f"{dataset['src_project_id']}.{dataset['src_dataset_name']}"
        dest_dataset_id = f"{dataset['dest_project_id']}.{dataset['dest_dataset_name']}"
        result = bq_datasets_compare(src_dataset_id, dest_dataset_id)
        click.echo(f"{src_dataset_id} == {dest_dataset_id} resolves to: {result}")


@root.group()
def bqts():
    "Scripts that generates bqts transfer-configs to an output file."
    pass


@bqts.command()
@click.option(
    "-f",
    "--from-json",
    type=click.File("r"),
    required=True,
    help="Path to the json file.",
)
@click.option(
    "-f", "--to-json", type=click.File("w"), default="-", help="Path to the json file."
)
def create(from_json, to_json):
    "Creates transfer configurations using params loaded from a file."
    to_json.write(from_json.read())
