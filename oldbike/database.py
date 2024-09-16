import sqlite3

conn = sqlite3.connect('bikedata.db')

query_to_create_table = '''
CREATE TABLE BikeDetails (
    owner INT,
    brand VARCHAR(13),
    kms_driven INT,
    power INT,
    age INT,
    predicted_price INT
)
'''

cur = conn.cursor()
cur.execute(query_to_create_table)
print("your database and table is created")
cur.close()
conn.close()
