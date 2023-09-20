from flask import Flask
import pymysql
miConexion = pymysql.connect( host='127.0.0.1', user= 'root', passwd='j3232777', db='tasksDB' )
cur = miConexion.cursor()
cur.execute( 'SELECT * FROM tasksDB.tareas' )


def dump():
 records = cur.fetchall()
 n=1
 for row in records:
    print( "resultado ",n, "?n ID: ", row[0], "/n descripcion: ", row[1], "/n Estado: ", row[2])
    n=n+1


app= Flask(__name__)   #reconoce que hay una aplicación
@app.route('/')
def index():
  return dump()

if __name__=="__main__":
    app.run(debug=True)


miConexion.close()
