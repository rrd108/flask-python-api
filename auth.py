from flask import request
import sqlite3


def is_accessible():
    if request.method == 'OPTIONS':
        return True

    noAuthResources = {
    'GET' : ('products'),
    'POST' : ('users=login'),
    'PATCH' : (),
    'DELETE' : ()
    }

    if request.url.rsplit('/', 1)[-1] in noAuthResources[request.method]:
        return True

    token = request.headers['Token'] if 'Token' in request.headers else None

    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('SELECT id FROM users WHERE token = ?', (token,))
    row = cur.fetchone()

    if row:
        return True

    return False