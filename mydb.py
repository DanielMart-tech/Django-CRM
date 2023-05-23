import psycopg2

conn = psycopg2.connect("dbname=elderco user=postgres password=1234")

cur = conn.cursor()

print("All done!")