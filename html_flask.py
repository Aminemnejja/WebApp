from flask import Flask, request, jsonify
from flask_cors import CORS  # Importez l'extension
import os
app = Flask(__name__)
matrix_valuesA = []
matrix_valuesB = []
vector_values = []
CORS(app, origins="*")

@app.route('/get_matrix_values_A', methods=['GET'])
def get_matrix_values_A():
    # Logique pour récupérer les valeurs de la matrice
    return jsonify(matrix_valuesA)

@app.route('/update_matrix_values_A', methods=['POST'])
def update_matrix_values_A():
    # Logique pour mettre à jour les valeurs de la matrice
    global matrix_valuesA
    matrix_valuesA = request.json['matrixValuesA']
    return jsonify({'message': 'Matrix values updated successfully!'})
@app.route('/get_matrix_values_B', methods=['GET'])
def get_matrix_values_B():
    # Logique pour récupérer les valeurs de la matrice
    return jsonify(matrix_valuesB)

@app.route('/update_matrix_values_B', methods=['POST'])
def update_matrix_values_B():
    # Logique pour mettre à jour les valeurs de la matrice
    global matrix_valuesB
    matrix_valuesB = request.json['matrixValuesB']
    return jsonify({'message': 'Matrix values updated successfully!'})

@app.route('/get_vector_values', methods=['GET'])
def get_vector_values():
    # Logique pour récupérer les valeurs du vecteur
    return jsonify(vector_values)

@app.route('/update_vector_values', methods=['POST'])
def update_vector_values():
    # Logique pour mettre à jour les valeurs du vecteur
    global vector_values
    vector_values = request.json['vectorValues']
    return jsonify({'message': 'Vector values updated successfully!'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)


