import psycopg2

host = 'hh-pgsql-public.ebi.ac.uk'
port = 5432
dbname = 'pfmegrnargs'
user = 'reader'
password = 'NWDMCE5xdipIjRrp'
DATABASE = f"host='{host}' port='{port}' dbname='{dbname}' user='{user}' password='{password}'"


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


query = "SELECT * FROM rnc_database"
with DBConnections() as dbconn:
    response = dbconn.pg_perform_query(query)
print('X'*100)
print(response)
