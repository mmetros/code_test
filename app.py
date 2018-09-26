from flask import Flask
from flask_restful import Api
from meter import Meters, Meter

app = Flask(__name__)
api = Api(app)


api.add_resource(Meters, '/meters')
api.add_resource(Meter, '/meters/<string:id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
