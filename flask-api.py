from flask import Flask, request, json
import sqlite3
from hashlib import md5

api = Flask(__name__)

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


@api.route('/products')             # default is GET
def get_products():
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