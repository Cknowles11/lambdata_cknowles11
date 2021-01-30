# Keep track of all the queries you create for the assignment
import os
import sqlite3

# construct a path to wherever your database exists
DB_FILEPATH = "rpg_db.sqlite3"
# DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = """SELECT avg(character_items)
FROM(
    SELECT
    character_id
    ,count(distinct item_id) as character_items
    FROM charactercreator_character_inventory
    GROUP BY character_id
    Limit 20
    ) subq"""

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)