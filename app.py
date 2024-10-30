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
