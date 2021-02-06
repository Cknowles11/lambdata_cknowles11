import os
import pandas as pd
import sqlite3

buddy = pd.read_csv(
    """
    https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-
    Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv
    """
)

DB_FILEPATH = "buddymove_holidayiq.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

buddy.to_sql('review', sqlite3.connect(DB_FILEPATH))

query_1 = """SELECT count(distinct "User Id") as
total_rows FROM review"""

query_2 = """SELECT count(shopping)
FROM(
    SELECT
    "User Id"
    ,"Nature"
    FROM review
    Where "Nature" >= 100
    ) subq
Where "Shopping" >= 100
    """

result1 = cursor.execute(query_1).fetchall()
print("RESULT 1", result1)

result2 = cursor.execute(query_2).fetchall()
print("RESULT 2", result2)
