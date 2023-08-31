from flask import Flask,render_template
import numpy as np
from joblib import load
import os

#cagar el modleo
dt = load('dt1.joblib')

#Generar servidor
servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo",methods=['GET'])
def formulario():
    return render_template('pagina1.html')

#Envio de datos a traves de JSON
@servidorWeb.route('/modelo',methods=['GET'])
def modeloPrediccion():
        #Procesar los datos de entrada
        contenido= request.json
        print(contenido)
        return jsonify({'resultado':"Hola"})

if __name__ == '__main__':
        servidorWeb.run(debug=False,host='0.0.0.0',port='8080')