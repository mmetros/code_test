import sqlite3
from datetime import datetime

# For the current timestamp
now = datetime.now()

# Make a connection to the database
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Turn on Foreign Key Support
cursor.execute("PRAGMA foreign_keys = ON")


# The meters table is the parent
# The meter_data table is the child

# Create Meter Table
cursor.execute("""CREATE TABLE IF NOT EXISTS meters (
                id INTEGER PRIMARY KEY,
                label text
                )""")

# Create Meter_data Table
cursor.execute("""CREATE TABLE IF NOT EXISTS meter_data (
                        id INTEGER PRIMARY KEY,
                        meter_id int,
                        [timestamp] timestamp,
                        value int,
                        FOREIGN KEY (meter_id) REFERENCES meters(id) on delete cascade
                        )""")


# Insert Values into meters table
meter_array = ["Meter 1", "Meter 2", "Meter 3", "Meter 1", "Meter 5"]
for meter in meter_array:
    cursor.execute("INSERT INTO meters VALUES (NULL,?)" ,(meter,))

# Insert Values into Meter_data Table
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (1, now,60))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (2, now, 10))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (3, now, 400))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (1, now, 20))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (2, now, 6000))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (3, now, 300))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (1, now, 1000))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (2, now, 23423))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (4, now, 434))
cursor.execute("INSERT INTO meter_data VALUES (NULL,?, ?, ?)", (4, now, 1244))

connection.commit()
connection.close()
