#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound    
from flask_cors import CORS
from models import db, Hero, Hero_powers, Power
import os

file_path = os.path.abspath(os.getcwd())+"\app.db"
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class Home(Resource):

    def get(self):

        response_dict = {
            "index": "Welcome the heroes",
        }

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response
    

    
    @app.errorhandler(NotFound)
    def handle_not_found(e):

        response = make_response(
            "Not Found: The requested resource does not exist.",
            404
        )

        return response    

api.add_resource(Home, '/')

class Hero_res(Resource):
    def get(self):
        heros_dict=[n.to_dict() for n in Hero.query.all()]
        response= make_response(
            jsonify(heros_dict),200,
        )
        return response
    def post(self):

        new_record = Hero(
            name=request.form['name'],
            super_name=request.form['super_name'],
        )

        db.session.add(new_record)
        db.session.commit()

        response_dict = new_record.to_dict()

        response = make_response(
            jsonify(response_dict),
            201,
        )

        return response


    @app.errorhandler(NotFound)
    def handle_not_found(e):

        response = make_response({
            "error": "Hero not found"},
            404
        )

        return response

api.add_resource(Hero_res, "/heroes") 

class HeroByid(Resource):
    def get(self, id):
        hero_dict=Hero.query.filter_by(id=id).first().to_dict()
        response = make_response(
            jsonify(hero_dict),200
        )
        return response
    def patch(self, id):
        pass

    def delete(self,id):
        pass 

    @app.errorhandler(500)
    def handle_not_found(e):

        response = make_response({
            "error": "Power not found"},
            500
        )

        return response
api.add_resource(HeroByid, '/heroes/<int:id>')






class Power_res(Resource):
    def get(self):
        power_dict=[n.to_dict() for n in Power.query.all()]
        response= make_response(
            jsonify(power_dict),200,
        )
        return response
api.add_resource(Power_res, '/powers')  
class PowerByid(Resource):
    def get(self, id):
        power_dict=Power.query.filter_by(id=id).first().to_dict()
        response = make_response(
            jsonify(power_dict),200
        )
        return response
    
    def patch(self, id):

        record = Power.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(record, attr, request.form[attr])

        db.session.add(record)
        db.session.commit()

        response_dict = record.to_dict()

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response    
api.add_resource(PowerByid, '/powers/<int:id>')


class Heropower(Resource):
    def get(self):
        heropower_dict=[n.to_dict() for n in Hero_powers.query.all()]
        response= make_response(
            jsonify(heropower_dict),200,
        )
        return response    
    
    def post(self):
        try:
            new_record = Hero_powers(
                strength=request.form['strength'],
                powers_id=request.form['powers_id'],
                hero_id=request.form['hero_id'],
            )

            db.session.add(new_record)
            db.session.commit()

            response_dict = new_record.to_dict()

            response = make_response(
                jsonify(response_dict),
                201,
            )
        
        
            return response
        except KeyError as e:
            # Handle missing key error
            error_message = f"Missing required field: {str(e)}"
            return jsonify({'error': 'Bad Request', 'message': error_message}), 400
        except Exception as e:
            # Handle other exceptions and return an error response
            return jsonify({'error': 'Internal Server Error please', 'message': str(e)}), 500
        
api.add_resource(Heropower, '/heropower')

if __name__ == '__main__':
    app.run(port=5555)
