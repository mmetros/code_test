import sqlite3
from datetime import datetime, date

# For the current dateime
now = datetime.now()

connection = sqlite3.connect('data.db', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# the id will always increment
# INTEGER PRIMARY KEY will create auto incrementing columns
# now when we have a new user, we will only have to create a username and password
create_meters = "CREATE TABLE IF NOT EXISTS meters ( id INTEGER PRIMARY KEY, label text)"
cursor.execute(create_meters)

# The meters table is the parent
# The meter_data table is the child

create_meter_data = """CREATE TABLE IF NOT EXISTS meter_data (
                        id INTEGER PRIMARY KEY,
                        meter_id int,
                        [timestamp] timestamp,
                        value int,
                        FOREIGN KEY (meter_id) REFERENCES meters(id) on delete cascade
                        )"""

cursor.execute(create_meter_data)

query = "INSERT INTO meters VALUES (NULL,?)"

# meter_array = ["Meter1", "Meter2", "Meter3"]
# for meter in meter_array:
#     cursor.execute(query,(meter,))

cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (1, now,30))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (2, now, 70))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (3, now, 200))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (1, now, 10))




connection.commit()
connection.close()


# Tests to see if the foreign key was successful
def see_table1():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "SELECT * FROM meters"
    result = cursor.execute(query)
    rows = result.fetchall()
    for row in rows:
        print(row)
def see_table2():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "SELECT * FROM meter_data"
    result = cursor.execute(query)
    rows = result.fetchall()
    for row in rows:
        print(row)

def delete(id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    query = "DELETE FROM meters WHERE id=?"
    cursor.execute(query, (id,))
    connection.commit()
    connection.close()

see_table1()
see_table2()
#
# delete(1)
#
# see_table1()
# see_table2()
