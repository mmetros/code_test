from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/meters')
def index():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM meters group by label")
    rows = cursor.fetchall()
    connection.close()
    return render_template('meters.html', meters=rows)

@app.route('/meters/<string:id>')
def meter_data(id):
    # open up a connection
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    # create a query to access the meter_data
    cursor.execute("SELECT * FROM meter_data WHERE meter_id=? ORDER BY timestamp DESC",(id,))
    row = cursor.fetchall()
    connection.close()
    return jsonify(row)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
