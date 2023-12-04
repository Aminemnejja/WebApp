# Script Streamlit (streamlit_app.py)
import streamlit as st                                                                                   
import requests
def get_matrix_values_A():
    try:
        # Effectuer une requête GET pour récupérer les valeurs de la matrice
        response = requests.get("https://webapp-esz7.onrender.com/get_matrix_values_A")
        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            matrix_valuesA = response.json()
            return matrix_valuesA
        else:
            st.error(f"Échec de la requête GET avec le code de statut {response.status_code}")
            st.error(response.text)
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la requête GET : {str(e)}")
        return None
def get_matrix_values_B():
    try:
        # Effectuer une requête GET pour récupérer les valeurs de la matrice
        response = requests.get("https://webapp-esz7.onrender.com/get_matrix_values_B")
        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            matrix_valuesB = response.json()
            return matrix_valuesB
        else:
            st.error(f"Échec de la requête GET avec le code de statut {response.status_code}")
            st.error(response.text)
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la requête GET : {str(e)}")
        return None

def get_vector_values():
    try:
        # Effectuer une requête GET pour récupérer les valeurs du vecteur
        response = requests.get("https://webapp-esz7.onrender.com/get_vector_values")
        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            vector_values = response.json()
            return vector_values
        else:
            st.error(f"Échec de la requête GET avec le code de statut {response.status_code}")
            st.error(response.text)
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la requête GET : {str(e)}")
        return None
def matriceA_html():

    html_code = """
   <!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matrice Dynamique</title>
    <style>
        .matrix-container {
            display: flex;
            flex-direction: column;
            align-items: left;
            margin: 20px;
        }
        
        body {
            padding: 0px;
            margin: 0px;
            max-width: 1444px;
            min-width: min-content;
            margin-left: auto;
            margin-right: auto;
        }
        
        .matrix {
            margin: 10px;
            display: flex;
            flex-direction: column;
        }
        
        .matrix-row {
            display: flex;
        }
        
        .matrix-cell {
            width: 40px;
            height: 40px;
            border: 1px solid black;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 2px;
        }
        
        input {
            width: 100%;
            height: 100%;
            border: none;
            box-sizing: border-box;
            text-align: center;
        }
        
        html {
            scroll-behavior: smooth;
            color: #242424;
            color: var(--color-text);
            padding: 12px;
            padding-top: 0px;
            padding-bottom: 0px;
            overflow-y: scroll;
            background-color: white;
            background-color: var(--color-background);
            background-size: 60px 40px;
            background-position: -1px -1px  ;
            font-size: 17px;
            line-height: 1.5;
        }
        
        .button-container {
            margin-top: 10px;
        }
        
        .add-button {
            display: inline-block;
            padding: 2px 12px;
            margin: 1px;
            line-height: 20px;
            color: #333333;
            color: var(--color-button);
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            background-color: hsl(0, 0%, 97%);
            background-image: linear-gradient(to bottom, hsl(0, 0%, 100%), hsl(0, 0%, 90%));
            border: 1px solid;
            border-color: silver;
            border-bottom-color: darkgray;
            border-radius: 2px;
            box-shadow: inset 0px 1px 0px hsla(0, 0%, 100%, 0.2), 0px 1px 2px hsla(0, 0%, 0%, 0.05);
        }
    </style>
</head>

<body>
    <legend align="left">La matrice A :</legend>

    <div class="matrix-container" id="matrix-container">
        <!-- La matrice sera générée dynamiquement ici -->
    </div>

    <div class="button-container">
        <button class="add-button" onclick="add()">+</button>
        <button class="add-button" onclick="retirer()">-</button>
        <button class="add-button" onclick="effacer()">effacer</button>
        <button class="add-button" onclick="getMatrixValuesFromPython()">Sauvgarder A </button>
    </div>

    <script>
        var matrixValues = [];
        var numRows = 2;
        var numCols = 2;

        function createMatrix() {
            var oldMatrix = document.getElementById("matrix");
            if (oldMatrix) {
                oldMatrix.remove();
            }

            var matrixContainer = document.getElementById("matrix-container");
            var matrix = document.createElement("div");
            matrix.id = "matrix";
            matrix.classList.add("matrix");

            for (var i = 0; i < numRows; i++) {
                var row = document.createElement("div");
                row.classList.add("matrix-row");

                for (var j = 0; j < numCols; j++) {
                    var cell = document.createElement("div");
                    cell.classList.add("matrix-cell");

                    var input = document.createElement("input");
                    input.type = "text";
                    input.classList.add("matrix-input");
                    input.id = "cell_" + i + "_" + j;

                    cell.appendChild(input);
                    row.appendChild(cell);
                }

                matrix.appendChild(row);
            }

            matrixContainer.appendChild(matrix);
            restoreMatrixValues();
        }

        function getMatrixValues() {
            matrixValues = [];
            var inputs = document.getElementsByClassName("matrix-input");
            for (var i = 0; i < inputs.length; i++) {
                matrixValues.push(inputs[i].value);
            }
            console.log("Matrix Values:", matrixValues);
        }

        function restoreMatrixValues() {
            var inputs = document.getElementsByClassName("matrix-input");

            for (var i = 0; i < numRows; i++) {
                for (var j = 0; j < numCols; j++) {
                    var value = matrixValues[i] && matrixValues[i][j] !== undefined ? matrixValues[i][j] : '';
                    inputs[i * numCols + j].value = value;
                }
            }
        }

        function saveMatrixValues() {
            var inputs = document.getElementsByClassName("matrix-input");
            matrixValues = [];

            for (var i = 0; i < numRows; i++) {
                var rowValues = [];
                for (var j = 0; j < numCols; j++) {
                    var inputValue = inputs[i * numCols + j].value;
                    rowValues.push(inputValue);
                }
                matrixValues.push(rowValues);
            }
        }

        function add() {
            saveMatrixValues();
            // Ajouter une colonne vide à la fin de chaque ligne
            for (var i = 0; i < numRows; i++) {
                matrixValues[i].push('');
            }

            // Ajouter une nouvelle ligne vide
            var newRow = Array(numCols).fill('');
            matrixValues.push(newRow);

            numCols++;
            numRows++;
            // Recréer la matrice avec les nouvelles dimensions
            createMatrix();
        }

        function effacer() {
            numCols = 2;
            numRows = 2;
            matrixValues = [];
            createMatrix();
        }

        function retirer() {
            if (numCols > 1 && numRows > 1) {
                numCols--;
                numRows--;
                createMatrix();
            }
        }

        function getMatrixValuesFromPython() {
           
            fetch('https://webapp-esz7.onrender.com/get_matrix_values_A')
                updateMatrixValuesInPython()
                .then(response => response.json())
                .then(data => {
                    matrixValuesA = data;
                    restoreMatrixValues();
                })
                .catch(error => console.error('Error:', error));
        }

        function updateMatrixValuesInPython() {
            saveMatrixValues();
            fetch('https://webapp-esz7.onrender.com/update_matrix_values_A', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        matrixValuesA: matrixValues
                    }),
                })
                .then(response => response.json())
                .then(data => console.log('Success:', data))
                .catch(error => console.error('Error:', error));
        }

        createMatrix();
    </script>
</body>

</html>
    """
    return html_code

def vecteur_html():
    html_code= """
    <!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vecteur Dynamique</title>
    <style>
        .vector-container {
            display: flex;
            flex-direction: row;
            align-items: left;
            margin: 20px;
        }
        
        body {
            padding: 0px;
            margin: 0px;
            max-width: 1444px;
            min-width: min-content;
            margin-left: auto;
            margin-right: auto;
        }
        
        .vector-cell {
            width: 40px;
            height: 40px;
            border: 1px solid black;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 2px;
        }
        
        input {
            width: 100%;
            height: 100%;
            border: none;
            box-sizing: border-box;
            text-align: center;
        }
        
        html {
            scroll-behavior: smooth;
            color: #242424;
            color: var(--color-text);
            padding: 12px;
            padding-top: 0px;
            padding-bottom: 0px;
            overflow-y: scroll;
            background-color: white;
            background-color: var(--color-background);
            background-size: 60px 40px;
            background-position: -1px -1px;
            font-size: 17px;
            line-height: 1.5;
        }
        
        .button-container {
            margin-top: 10px;
        }
        
        .add-button {
            display: inline-block;
            padding: 2px 12px;
            margin: 1px;
            line-height: 20px;
            color: #333333;
            color: var(--color-button);
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            background-color: hsl(0, 0%, 97%);
            background-image: linear-gradient(to bottom, hsl(0, 0%, 100%), hsl(0, 0%, 90%));
            border: 1px solid;
            border-color: silver;
            border-bottom-color: darkgray;
            border-radius: 2px;
            box-shadow: inset 0px 1px 0px hsla(0, 0%, 100%, 0.2), 0px 1px 2px hsla(0, 0%, 0%, 0.05);
        }
    </style>
</head>

<body>
    <legend align="left">Le vecteur b:</legend>

    <div class="vector-container" id="vector-container">
        <!-- Le vecteur sera généré dynamiquement ici -->
    </div>

    <div class="button-container">
        <button class="add-button" onclick="add()">+</button>
        <button class="add-button" onclick="retirer()">-</button>
        <button class="add-button" onclick="effacer()">effacer</button>
        <button class="add-button" onclick="getVectorValuesFromPython()">Sauvgarder B</button>
    </div>

    <script>
        var vectorValues = [];
        var numElements = 2;

        function createVector() {
            var oldVector = document.getElementById("vector");
            if (oldVector) {
                oldVector.remove();
            }

            var vectorContainer = document.getElementById("vector-container");
            var vector = document.createElement("div");
            vector.id = "vector";
            vector.classList.add("vector");

            for (var i = 0; i < numElements; i++) {
                var cell = document.createElement("div");
                cell.classList.add("vector-cell");

                var input = document.createElement("input");
                input.type = "text";
                input.classList.add("vector-input");
                input.id = "element_" + i;

                cell.appendChild(input);
                vector.appendChild(cell);
            }

            vectorContainer.appendChild(vector);
            restoreVectorValues();
        }

        function getVectorValues() {
            vectorValues = [];
            var inputs = document.getElementsByClassName("vector-input");
            for (var i = 0; i < inputs.length; i++) {
                vectorValues.push(inputs[i].value);
            }
            console.log("Vector Values:", vectorValues);
        }

        function restoreVectorValues() {
            var inputs = document.getElementsByClassName("vector-input");

            for (var i = 0; i < numElements; i++) {
                var value = vectorValues[i] !== undefined ? vectorValues[i] : '';
                inputs[i].value = value;
            }
        }

        function saveVectorValues() {
            var inputs = document.getElementsByClassName("vector-input");
            vectorValues = [];

            for (var i = 0; i < numElements; i++) {
                var inputValue = inputs[i].value;
                vectorValues.push(inputValue);
            }
        }

        function add() {
            saveVectorValues();
            // Ajouter un nouvel élément vide
            vectorValues.push('');
            numElements++;
            // Recréer le vecteur avec la nouvelle dimension
            createVector();
        }

        function effacer() {
            numElements = 2;
            vectorValues = [];
            createVector();
        }

        function retirer() {
            if (numElements > 1) {
                numElements--;
                vectorValues.pop();
                createVector();
            }
        }

        function getVectorValuesFromPython() {
            fetch('https://webapp-esz7.onrender.com/get_vector_values')
            updateVectorValuesInPython()
                .then(response => response.json())
                .then(data => {
                    vectorValues = data;
                    restoreVectorValues();
                })
                .catch(error => console.error('Error:', error));
        }

        function updateVectorValuesInPython() {
            saveVectorValues();
            fetch('https://webapp-esz7.onrender.com/update_vector_values', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        vectorValues: vectorValues
                    }),
                })
                .then(response => response.json())
                .then(data => console.log('Success:', data))
                .catch(error => console.error('Error:', error));
        }


        createVector();
    </script>
</body>

</html>
    
    """
    return html_code

def matriceB_html():
    html_code="""
    <!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matrice Dynamique</title>
    <style>
        .matrix-container {
            display: flex;
            flex-direction: column;
            align-items: left;
            margin: 20px;
        }
        
        body {
            padding: 0px;
            margin: 0px;
            max-width: 1444px;
            min-width: min-content;
            margin-left: auto;
            margin-right: auto;
        }
        
        .matrix {
            margin: 10px;
            display: flex;
            flex-direction: column;
        }
        
        .matrix-row {
            display: flex;
        }
        
        .matrix-cell {
            width: 40px;
            height: 40px;
            border: 1px solid black;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 2px;
        }
        
        input {
            width: 100%;
            height: 100%;
            border: none;
            box-sizing: border-box;
            text-align: center;
        }
        
        html {
            scroll-behavior: smooth;
            color: #242424;
            color: var(--color-text);
            padding: 12px;
            padding-top: 0px;
            padding-bottom: 0px;
            overflow-y: scroll;
            background-color: white;
            background-color: var(--color-background);
            background-size: 60px 40px;
            background-position: -1px -1px;
            font-size: 17px;
            line-height: 1.5;
        }
        
        .button-container {
            margin-top: 10px;
        }
        
        .add-button {
            display: inline-block;
            padding: 2px 12px;
            margin: 1px;
            line-height: 20px;
            color: #333333;
            color: var(--color-button);
            text-align: center;
            vertical-align: middle;
            cursor: pointer;
            background-color: hsl(0, 0%, 97%);
            background-image: linear-gradient(to bottom, hsl(0, 0%, 100%), hsl(0, 0%, 90%));
            border: 1px solid;
            border-color: silver;
            border-bottom-color: darkgray;
            border-radius: 2px;
            box-shadow: inset 0px 1px 0px hsla(0, 0%, 100%, 0.2), 0px 1px 2px hsla(0, 0%, 0%, 0.05);
        }
    </style>
</head>

<body>
    <legend align="left">La matrice B:</legend>

    <div class="matrix-container" id="matrix-container">
        <!-- La matrice sera générée dynamiquement ici -->
    </div>

    <div class="button-container">
        <button class="add-button" onclick="add()">+</button>
        <button class="add-button" onclick="retirer()">-</button>
        <button class="add-button" onclick="effacer()">effacer</button>
        <button class="add-button" onclick="getMatrixValuesFromPython()">Sauvgarder B</button>
    </div>

    <script>
        var matrixValues = [];
        var numRows = 2;
        var numCols = 2;

        function createMatrix() {
            var oldMatrix = document.getElementById("matrix");
            if (oldMatrix) {
                oldMatrix.remove();
            }

            var matrixContainer = document.getElementById("matrix-container");
            var matrix = document.createElement("div");
            matrix.id = "matrix";
            matrix.classList.add("matrix");

            for (var i = 0; i < numRows; i++) {
                var row = document.createElement("div");
                row.classList.add("matrix-row");

                for (var j = 0; j < numCols; j++) {
                    var cell = document.createElement("div");
                    cell.classList.add("matrix-cell");

                    var input = document.createElement("input");
                    input.type = "text";
                    input.classList.add("matrix-input");
                    input.id = "cell_" + i + "_" + j;

                    cell.appendChild(input);
                    row.appendChild(cell);
                }

                matrix.appendChild(row);
            }

            matrixContainer.appendChild(matrix);
            restoreMatrixValues();
        }

        function getMatrixValues() {
            matrixValues = [];
            var inputs = document.getElementsByClassName("matrix-input");
            for (var i = 0; i < inputs.length; i++) {
                matrixValues.push(inputs[i].value);
            }
            console.log("Matrix Values:", matrixValues);
        }

        function restoreMatrixValues() {
            var inputs = document.getElementsByClassName("matrix-input");

            for (var i = 0; i < numRows; i++) {
                for (var j = 0; j < numCols; j++) {
                    var value = matrixValues[i] && matrixValues[i][j] !== undefined ? matrixValues[i][j] : '';
                    inputs[i * numCols + j].value = value;
                }
            }
        }

        function saveMatrixValues() {
            var inputs = document.getElementsByClassName("matrix-input");
            matrixValues = [];

            for (var i = 0; i < numRows; i++) {
                var rowValues = [];
                for (var j = 0; j < numCols; j++) {
                    var inputValue = inputs[i * numCols + j].value;
                    rowValues.push(inputValue);
                }
                matrixValues.push(rowValues);
            }
        }

        function add() {
            saveMatrixValues();
            // Ajouter une colonne vide à la fin de chaque ligne
            for (var i = 0; i < numRows; i++) {
                matrixValues[i].push('');
            }

            // Ajouter une nouvelle ligne vide
            var newRow = Array(numCols).fill('');
            matrixValues.push(newRow);

            numCols++;
            numRows++;
            // Recréer la matrice avec les nouvelles dimensions
            createMatrix();
        }

        function effacer() {
            numCols = 2;
            numRows = 2;
            matrixValues = [];
            createMatrix();
        }

        function retirer() {
            if (numCols > 1 && numRows > 1) {
                numCols--;
                numRows--;
                createMatrix();
            }
        }

        function getMatrixValuesFromPython() {

            fetch('https://webapp-esz7.onrender.com/get_matrix_values_B')
            updateMatrixValuesInPython()
                .then(response => response.json())
                .then(data => {
                    matrixValuesB = data;
                    restoreMatrixValues();
                })
                .catch(error => console.error('Error:', error));
        }

        function updateMatrixValuesInPython() {
            saveMatrixValues();
            fetch('https://webapp-esz7.onrender.com/update_matrix_values_B', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        matrixValuesB: matrixValues
                    }),
                })
                .then(response => response.json())
                .then(data => console.log('Success:', data))
                .catch(error => console.error('Error:', error));
        }

        createMatrix();
    </script>
</body>

</html>
    """
    return html_code

