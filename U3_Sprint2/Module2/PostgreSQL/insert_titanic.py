import psycopg2
import os
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
titanic_df = pd.read_csv("https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv")
titanic_dict = titanic_df.to_dict("titanic_dict")
titanic_tuples = [(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]) for r in titanic_dict]


insert_query = f"INSERT INTO {table_name} (name, data) VALUES %s"

execute_values(cursor, insert_query, titanic_tuples)

connection.commit()