import psycopg2

"""
Need to implement the setting through the reading configuration file, it's just hardcoded example with third party
postgresql database - https://rnacentral.org/help/public-database
"""

HOST = 'hh-pgsql-public.ebi.ac.uk'
PORT = 5432
DBNAME = 'pfmegrnargs'
USER = 'reader'
PASSWORD = 'NWDMCE5xdipIjRrp'
DATABASE = f"host='{HOST}' port='{PORT}' dbname='{DBNAME}' user='{USER}' password='{PASSWORD}'"


class DBConnections:
    _postgres_db = None

    @property
    def postgres_db(self):
        if self._postgres_db is None:
            self._postgres_db = psycopg2.connect(DATABASE)
        return self._postgres_db

    @staticmethod
    def _query(db_conn, sql):
        with db_conn, db_conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._postgres_db is not None:
            self._postgres_db.close()

    def pg_perform_query(self, sql):
        """Returns query result from postgresDB"""
        return self._query(self.postgres_db, sql=sql)
