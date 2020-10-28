import os

from flask import Flask, jsonify, request
# from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

# http status code
success_code = 200
not_found_code = 404
invalid_code = 422
forbidden_code = 403

project_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "site.db"

app = Flask(__name__)
# cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class KeyValuePair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(20), unique=True,
                    nullable=False)
    value = db.Column(db.String(200), unique=False,
                      nullable=False)

    def get_json_representation(self):
        return {"key": self.key, "value": self.value}

    def __repr__(self):
        return "KeyPairValue: ({}={})".format(self.key, self.value)


# class Authorization(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


@app.route("/", methods=['GET'])
def get_pairs():
    header = request.headers
    print(header)
    print(KeyValuePair.query.all())
    res = [pair.get_json_representation()
           for pair in db.session.query(KeyValuePair).all()]
    return jsonify(res), success_code


@app.route("/", methods=['POST'])
def post_pair():
    header = request.headers
    print(header)
    try:
        for key in request.form:
            value = request.form[key]
            if key != "" and value != "":
                db.session.add(KeyValuePair(key=key, value=value))
            else:
                raise ValueError("Wrong format")
        db.session.commit()

    except Exception as e:
        return jsonify({"Error": str(e)}), invalid_code

    return jsonify({"State": "Successful"}), success_code


@app.route("/", methods=['PUT'])
def put_pair():
    header = request.headers
    print(header)
    try:
        for key in request.form:
            value = request.form[key]
            if key != "" and value != "":
                db.session.query(KeyValuePair).filter(KeyValuePair.key == key).update(
                    {KeyValuePair.value: value})
            else:
                raise ValueError("Wrong format")
        db.session.commit()

    except Exception as e:
        return jsonify({"Error": str(e)}), invalid_code

    return jsonify({"State": "Successful"}), success_code


@app.route("/", methods=['DELETE'])
def delete_pair():
    code = success_code
    header = request.headers
    print(header)
    try:
        for key in request.form:
            value = request.form[key]
            if key != "":
                query = db.session.query(KeyValuePair).filter(
                    KeyValuePair.key == key)

                if len(query.all()) >= 1:
                    query.delete()
                else:
                    code = not_found_code
                    raise ValueError("Key does not exist to delete")
            else:
                code = invalid_code
                raise ValueError("Wrong format")
        db.session.commit()

    except Exception as e:
        if type(e) != ValueError:
            code = invalid_code
        return jsonify({"Error": str(e)}), code

    return jsonify({"State": "Successful"}), code


@ app.route("/<path:path>", methods=['GET'])
def get_pair(path):
    code = success_code
    try:
        query = KeyValuePair.query.filter_by(key=path).all()
        if len(query) != 1:
            raise ValueError("Key does not exist")
    except Exception as e:
        if type(e) == ValueError:
            code = not_found_code
        else:
            code = invalid_code
        return jsonify({"Error": str(e)}), code

    return jsonify(query[0].get_json_representation()), code


if __name__ == '__main__':
    if not os.path.exists(db_file):
        db.creat_all()
    app.run(host='0.0.0.0', port=5000, debug=True,
            ssl_context=('keys/cert.pem', 'keys/key.pem'))
