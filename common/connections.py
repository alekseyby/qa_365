import psycopg2

host = 'hh-pgsql-public.ebi.ac.uk'
port = 5432
dbname = 'pfmegrnargs'
user = 'reader'
password = 'NWDMCE5xdipIjRrp'
DSN = f"host='{host}' port='{port}' dbname='{dbname}' user='{user}' password='{password}'"

query = "SELECT * FROM rnc_database"

connection = psycopg2.connect(DSN)
try:

    with connection, connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
finally:
    cursor.close()
