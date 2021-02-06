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

table_name = "Titanic"
# query = f"""
# CREATE TABLE IF NOT EXISTS {table_name} (
#     id SERIAL PRIMARY KEY
#     ,name varchar(40) NOT NULL
#     ,data JSONB
#     );
# """
# print("SQL:", query)
# cursor.execute(query)

insert_query = f"INSERT INTO {table_name} (name, data) VALUES %s"
titanic_df = pd.read_csv("https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module2-sql-for-analysis/titanic.csv")

titanic_sql = titanic_df.to_sql(
    name = "Titanic", con = connection
    )

execute_values(cursor, insert_query, titanic_sql)

# print("-------------------")
# query = f"SELECT * FROM {table_name};"
# print("SQL:", query)
# cursor.execute(query)
# for row in cursor.fetchall():
#     print(row)

# connection.commit()