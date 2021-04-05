# Standard library
import logging

# Third party
from google.cloud import bigquery

# Logger setup
logger = logging.getLogger(__name__)


def list_tables(dataset_id, client=bigquery.Client()):
    tables = client.list_tables(dataset_id)

    return {table.table_id for table in tables}


def compare(src_dataset_id, dest_dataset_id, client=bigquery.Client()):
    src_tables = list_tables(src_dataset_id)
    dest_tables = list_tables(dest_dataset_id)

    equal = True
    if src_tables.symmetric_difference(dest_tables):
        logger.info(
            f"These datasets contain the following symmetric difference: {src_tables ^ dest_tables}"
        )
        equal = False

    tables_intersection = src_tables.intersection(dest_tables)

    for table in tables_intersection:
        src_table = client.get_table(f"{src_dataset_id}.{table}")
        dest_table = client.get_table(f"{dest_dataset_id}.{table}")

        if src_table.num_rows == dest_table.num_rows and src_table.num_bytes == dest_table.num_bytes:
            logger.debug(
                f"{src_dataset_id}.{table} is equal to {dest_dataset_id}.{table}"
            )
        else:
            logger
            logger.info(
                f"{src_dataset_id}.{table} is NOT equal to {dest_dataset_id}.{table}. The former contains {src_table.num_rows} rows totalling {src_table.num_bytes} as compared to {src_table.num_rows} rows & {src_table.num_bytes}."
            )
            equal = False
    
    return equal
        
if __name__ == "__main__":
    compare("sourceproject.mydataset", "sourceproject.mydataset")
