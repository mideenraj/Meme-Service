from flask import Flask
from flask_restful import Resource, Api
import os, requests, random

app = Flask(__name__)
api = Api(app)

class MemeService(Resource):
    
    def get(self):
        req = requests.get('http://alpha-meme-maker.herokuapp.com/')
        memes = req.json()['data']
        random_meme = random.choice(memes)
        return random_meme
        
api.add_resource(MemeService, '/')



if __name__ == '__main__':
    app.run(port=7000, debug=True)
    