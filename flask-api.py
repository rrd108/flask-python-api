from flask import Flask, request, json, Response
from flask_cors import CORS
import sqlite3
from hashlib import md5
from auth import is_accessible

api = Flask(__name__)
CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'
api.config['CORS_METHODS'] = ['GET', 'POST']
api.config['CORS_ORIGINS'] = ['localhost', 'localhost:3000']

@api.route('/users/login', methods=['POST'])
def get_token():
    data = request.json
    con = sqlite3.connect('data.db')
    con.row_factory = sqlite3.Row     # needed for using keys() later
    cur = con.cursor()
    cur.execute('SELECT id, token FROM users WHERE email = ? AND password = ?', (data['email'], md5(data['password'].encode('UTF-8')).hexdigest()))
    row = cur.fetchone()
    user = dict(zip(row.keys(), row))
    return json.dumps(user)


@api.route('/users')
def get_users():
    if not is_accessible():
        return Response('Access denied', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    con = sqlite3.connect('data.db')
    con.row_factory = sqlite3.Row     # needed for using keys() later
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    users = []
    for row in rows:
        d = dict(zip(row.keys(), row))   # a dict with column names as keys
        users.append(d)
    return json.dumps(users)


@api.route('/products', methods=['GET', 'POST'])             # default is GET
def get_products():
    if not is_accessible():
        return Response('Access denied', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    con = sqlite3.connect('data.db')
    con.row_factory = sqlite3.Row     # needed for using keys() later
    cur = con.cursor()
    cur.execute('SELECT * FROM products')
    rows = cur.fetchall()
    products = []
    for row in rows:
        d = dict(zip(row.keys(), row))   # a dict with column names as keys
        products.append(d)
    return json.dumps(products)


if __name__ == '__main__':
    api.run(debug=True) # TODO remove in production