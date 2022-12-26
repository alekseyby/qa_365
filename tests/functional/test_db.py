import pytest
import allure
from common import log_helper
from common.db_adapter import DBConnections
from common.file_reader import CSV


@allure.title("Test: retrieve a list of RNAcentral databases")
@allure.description("""Test checks connection to https://rnacentral.org/help/public-database""")
@pytest.mark.db_test
def test_db_connection():
    query = "SELECT * FROM rnc_database"
    with DBConnections() as db_conn:
        # retrieve a list of RNAcentral databases
        data = db_conn.pg_perform_query(query)
        log = log_helper.get_logger(__name__)
        log.info(f' RNAcentral databases: {data}')

