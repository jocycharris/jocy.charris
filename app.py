from flask import Flask
import pymysql
miConexion = pymysql.connect( host='127.0.0.1', user= 'root', passwd='j3232777', db='tallerdb' )
cur = miConexion.cursor()
cur.execute( 'SELECT nombre, apellido,edad FROM Estudiante' )



app= Flask(__name__)   #reconoce que hay una aplicación
@app.route('/')
def index():
    return cur.fetchall()

if __name__=="__main__":
    app.run(debug=True)

miConexion.close()