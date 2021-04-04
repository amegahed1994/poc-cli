import click
import logging

@click.group(commands=ROOT_COMMANDS)
@click.option(
    "--log-level",
    type=click.Choice(["ERROR", "WARNING", "INFO", "DEBUG"]),
    default="INFO",
    show_default=True,
    help="The desired logging level.",
)
def root(log_level):
    "Goal of this command-line interface is to centralize mmvt's scripts."
    pass
    logging.basicConfig(level=log_level)
    logging.debug("ERROR FROM ROOT")

@root.group()
def bq():
    "Scripts that performs QA on datasets post copy/migration."
    pass


@bq.group()
def datasets():
    pass


@datasets.command()
@click.option("-f", "--from-json", type=click.File("r"), help="Path to the json file.")
def compare(from_json):
    "Compares datasets lazily by checking their metadata."
    print("Comparing tables from json")
    logging.debug("ERROR FROM compare")
