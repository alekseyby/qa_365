import psycopg2

host = 'hh-pgsql-public.ebi.ac.uk'
port = 5432
dbname = 'pfmegrnargs'
user = 'reader'
password = 'NWDMCE5xdipIjRrp'
DSN = f"host='{host}' port='{port}' dbname='{dbname}' user='{user}' password='{password}'"

query = "SELECT * FROM rnc_database"

conn = psycopg2.connect(DSN)
try:

    with conn:
        with conn.cursor() as curs:
            curs.execute(query)
            rows = curs.fetchall()
            print(rows)
finally:
    conn.close()

