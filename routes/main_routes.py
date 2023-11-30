# app/routes/main_routes.py
from flask import Flask, render_template, request
from app import app
import joblib

# Carregue o modelo
model = joblib.load('seu_modelo.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtenha dados do formulário
        sepalLength = request.form['sepalLength']
        sepalWidth  = request.form['sepalWidth']
        petalLength = request.form['petalLength']
        petalWidth  = request.form['petalWidth']

        # Faça previsões usando o modelo
        prediction = model.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])
        
        # Passe os resultados para o template
        return render_template('index.html', prediction=prediction)

    return render_template('index.html')
