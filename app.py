import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Claire in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://renderlab_user:MnNSDQTXLLXHeWRKBSAfOSs3QdvKQfkD@dpg-csh8h9dumphs73c2ebr0-a/renderlab")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def table():
    conn = psycopg2.connect("postgresql://renderlab_user:MnNSDQTXLLXHeWRKBSAfOSs3QdvKQfkD@dpg-csh8h9dumphs73c2ebr0-a/renderlab")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"