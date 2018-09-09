#encoding: utf-8
import os
from flask import Flask
import psycopg2
from data import DATA, USER, PASS, HOST, PORT, SSL

app = Flask(__name__)

@app.route('/<path:arg>')
def consulta(arg):
	conn = psycopg2.connect(database= DATA, user= USER, password=PASS, host=HOST, port=PORT, sslmode=SSL)
	cursor = conn.cursor()
	cursor.execute("select * from estado where uf = '"+arg.upper()+"'")
	records = cursor.fetchall()
	if len(records) == 0:
		return "Não existe um estado com a sigla "+str(arg)
	return ""+records[0][1]+" - "+records[0][0]

@app.route('/')
def index():
	return 'Não tem nada aqui'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
