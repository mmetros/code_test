import sqlite3
from flask import render_template, jsonify, make_response
from flask_restful import Resource

class Meter(Resource):

    @classmethod
    def find_by_id(cls, id):
        # open up a connection
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        # create a query to access the meter_data
        cursor.execute("SELECT * FROM meter_data WHERE meter_id=? ORDER BY timestamp DESC",(id,))
        # Access all those rows from our query
        rows = cursor.fetchall()
        connection.close()
        return rows

    def get(self, id):
        rows = self.find_by_id(id)
        if rows:
            return jsonify(rows)
        else:
            return jsonify("No Data Found for this Meter")

class Meters(Resource):

    def get(self):
        # open up a connection
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        # create a query to access the meter_data
        cursor.execute("SELECT DISTINCT id, label FROM meters")
        # Access all those rows from our query
        rows = cursor.fetchall()
        connection.close()
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('meters.html', meters=rows), 200, headers)
