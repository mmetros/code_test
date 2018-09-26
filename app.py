from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/meters')
def index():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "SELECT DISTINCT label, id FROM meters "
    results = cursor.execute(query)
    rows = cursor.fetchall()
    return render_template('meters.html', meters=rows)

@app.route('/meters/<string:id>')
def meter_data(id):
    # open up a connection
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    # create a query to access the meter_data
    query = "SELECT * FROM meter_data WHERE meter_id=? ORDER BY timestamp DESC"
    result = cursor.execute(query,(id,))

    row = result.fetchall()
    connection.close()
    print({'id': row[0][0]})
    print({'meter_id': row[0][1]})
    print({'meter_id': row[0][1]})
    return jsonify(row)


# @app.route('/_background_process')
# def _background_process():
#     name = request.args.get('name')


# @app.route('/meters/<string:name>')
# def index():
#     return render_template('')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
