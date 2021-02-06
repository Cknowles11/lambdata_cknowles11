import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd

DB_NAME = "vqbzfutz"
DB_USER = "vqbzfutz"
DB_PASSWORD = "CFfGFT7HX6Fre4EJF1rT546avygAy5Cu"
DB_HOST = "otto.db.elephantsql.com"

connection = psycopg2.connect(
    dbname = DB_NAME, user = DB_USER,
    password = DB_PASSWORD, host = DB_HOST
    )

cursor = connection.cursor()
print("Cursor:", cursor)

#Example query
# query = "SELECT * from table_dspt9"
# cursor.execute(query)
# print(cursor.fetchall())


#Create a table

table_name = "test_table9_2"
# print("-------------------")
# query = f"""
# CREATE TABLE IF NOT EXISTS {table_name} (
#   id SERIAL PRIMARY KEY,
#   name varchar(40) NOT NULL,
#   data JSONB
# );
# """
# print("SQL:", query)
# cursor.execute(query)

#Insert Data

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

# insertion_query = f"INSERT INTO {table_name} (name, data) VALUES (%s, %s)"
# cursor.execute(insertion_query,
#  ('A rowwwww', 'null')
# )
# cursor.execute(insertion_query,
#  ('Another row, with JSONNNNN', json.dumps(my_dict))
# )

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
insertion_query = f"INSERT INTO {table_name} (name, data) VALUES %s"
# execute_values(cursor, insertion_query, [
#  ('A rowwwww', 'null'),
#  ('Another row, with JSONNNNN', json.dumps(my_dict)),
#  ('Third row', "3")
# ])

# Insert dataframe

# table_name = "test_table9_2"
insertion_query = f"INSERT INTO {table_name} (name, data) VALUES %s"

df = pd.DataFrame([
  ['A rowwwww', 'null'],
  ['Another row, with JSONNNNN', json.dumps(my_dict)],
  ['Third row', "null"],
  ["Pandas Row", "null"]
])

records = df.to_dict("records") #> [{0: 'A rowwwww', 1: 'null'}, {0: 'Another row, with JSONNNNN', 1: '{"a": 1, "b": ["dog", "cat", 42], "c": "true"}'}, {0: 'Third row', 1: '3'}, {0: 'Pandas Row', 1: 'YOOO!'}]
list_of_tuples = [(r[0], r[1]) for r in records]

execute_values(cursor, insertion_query, list_of_tuples)

#
# QUERY THE TABLE
#

print("-------------------")
query = f"SELECT * FROM {table_name};"
print("SQL:", query)
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# # ACTUALLY SAVE THE TRANSACTIONS
connection.commit()

cursor.close()
connection.close()