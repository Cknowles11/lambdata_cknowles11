import os
import sqlite3

# construct a path to wherever your database exists
DB_FILEPATH = "buddymove_holidayiq.sqlite3"
# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query_1 = """SELECT count(distinct "User Id") as 
total_rows FROM review"""

query_2 = """SELECT count(distinct "User Id")
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