from flask import Flask, json # flask should be installed
import sqlite3

api = Flask(__name__)


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