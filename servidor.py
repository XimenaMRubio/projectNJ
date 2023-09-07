from flask import Flask,render_template, request, jsonify
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
@servidorWeb.route('/modelo',methods=['POST'])
def modeloPrediccion():
        #Procesar los datos de entrada
        contenido= request.json
        print(contenido)
        datosEntrada = np.array([
               .88,0,2.6,.098,25,67,0.9968,1,.89,
               contenido['pH'],
               contenido['sulphates'],
               contenido['alcohol']
        ])
        #Utilizar modelol
        resultado=dt.predict(datosEntrada.reshape(1,-1))
        return jsonify({'resultado':str(resultado[0])})

#Envio de datos a traves de JSON
@servidorWeb.route('/modeloForm',methods=['POST'])
def modeloPrediccion():
        #Procesar los datos de entrada
        contenido= request.form
        print(contenido)
        datosEntrada = np.array([
               .88,0,2.6,.098,25,67,0.9968,1,.89,
               contenido['pH'],
               contenido['sulphates'],
               contenido['alcohol']
        ])
        #Utilizar modelol
        resultado=dt.predict(datosEntrada.reshape(1,-1))
        return jsonify({'resultado':str(resultado[0])})

if __name__ == '__main__':
        servidorWeb.run(debug=False,host='0.0.0.0',port='8080')