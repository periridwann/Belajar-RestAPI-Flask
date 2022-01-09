from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.wrappers import response

# inisiasi object
app = Flask(__name__)

# inisiasi object flask restful
api = Api(app)

# inisiasi object cors
CORS(app)

# inisiasi variable kosong bertipe dictionary
identitas = {} #variable global, dictionary = json

# membuat class resource
class ContohResource(Resource):
    # buat method get dan post
    def get(self):
        # response = {"msg": "Hello World! It's my first Restful"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        kelas = request.form["kelas"]
        identitas["nama"] = nama
        identitas["umur"] = kelas
        response = {"msg": "Data sukses bosku"}
        return response

api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)