from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)

DATA = {
        'buah':
            ['pisang',
            'semangka',
            'melon',
            'jeruk',
            'anggur',
            'durian',
            'rambutan',
            'lemon',
            'kiwi',
            'cery']
}

class buah(Resource):
        def get(self):
                return {'data': DATA}, 200

        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('location', required=True, location='form')
            args = parser.parse_args()
            if args['location'] in DATA['buah']:
                return {
                    'message': f"'{args['location']}' already exists."
                }, 401
            else:
                DATA['buah'].append(args['location'])
                return {'data': DATA}, 200
                
        def delete(self):
            parser = reqparse.RequestParser()
            parser.add_argument('location', required=True, location='form')
            args = parser.parse_args()

            if args['location'] in DATA['buah']:
                DATA['buah'].remove(args['location'])
                return {'data': DATA}, 200
            else:
                return {
                    'message': f"'{args['location']}' does not exist."
                    }, 404


api.add_resource(buah, '/buah')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
