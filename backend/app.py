from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@10.0.2.168:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Counts(db.Model):
    id = db.Column(db.Integer, primary_key=True)


@app.route('/', methods=['GET'])
def fetch():
    return jsonify({'count': Counts.query.count()})


@app.route('/', methods=['POST'])
def add():
    s = Counts()
    db.session.add(s)
    db.session.commit()
    return jsonify({'count': Counts.query.count()})


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'count': 5})

if __name__ == '__main__':
    print('starting')
    db.create_all()
    app.run(host='0.0.0.0', debug=True)