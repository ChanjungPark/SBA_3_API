from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)   # 데코레이터 만드는 문법
api = Api(app)

class Rest(Resource):
    def get(self):
        return {'rest':'OK'}

api.add_resource(Rest,'/')

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=8080)