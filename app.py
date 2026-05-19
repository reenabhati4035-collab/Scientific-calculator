# app.py
# Scientific Calculator Web App using Flask
# Run:
#   pip install flask
#   python app.py
#
# Open:
#   http://127.0.0.1:5000

from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scientific Calculator</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial, sans-serif;
        }

        body{
            background:#0f172a;
            display:flex;
            justify-content:center;
            align-items:center;
            min-height:100vh;
            padding:20px;
        }

        .calculator{
            width:100%;
            max-width:420px;
            background:#1e293b;
            border-radius:20px;
            padding:20px;
            box-shadow:0 0 20px rgba(0,0,0,0.5);
        }

        h1{
            text-align:center;
            color:white;
            margin-bottom:20px;
        }

        .display{
            width:100%;
            padding:15px;
            font-size:24px;
            border:none;
            border-radius:10px;
            margin-bottom:15px;
            background:#334155;
            color:white;
        }

        .result-box{
            width:100%;
            min-height:50px;
            background:#0f172a;
            color:#00ff88;
            border-radius:10px;
            padding:12px;
            margin-bottom:20px;
            font-size:22px;
            word-wrap:break-word;
        }

        .buttons{
            display:grid;
            grid-template-columns:repeat(4,1fr);
            gap:10px;
        }

        button{
            padding:15px;
            border:none;
            border-radius:12px;
            font-size:18px;
            cursor:pointer;
            transition:0.2s;
        }

        button:hover{
            transform:scale(1.05);
        }

        .num{
            background:#475569;
            color:white;
        }

        .operator{
            background:#f59e0b;
            color:white;
        }

        .science{
            background:#2563eb;
            color:white;
        }

        .equal{
            background:#16a34a;
            color:white;
            grid-column:span 2;
        }

        .clear{
            background:#dc2626;
            color:white;
        }

        @media(max-width:500px){
            button{
                padding:12px;
                font-size:16px;
            }

            .display{
                font-size:20px;
            }
        }
    </style>
</head>
<body>

<div class="calculator">
    <h1>Scientific Calculator</h1>

    <form method="POST">
        <input
            type="text"
            name="expression"
            class="display"
            id="display"
            value="{{ expression }}"
            placeholder="Enter Expression"
            autocomplete="off"
        >

        <div class="result-box">
            {{ result }}
        </div>

        <div class="buttons">

            <button type="button" class="science" onclick="insertValue('sin(')">sin</button>
            <button type="button" class="science" onclick="insertValue('cos(')">cos</button>
            <button type="button" class="science" onclick="insertValue('tan(')">tan</button>
            <button type="button" class="science" onclick="insertValue('sqrt(')">√</button>

            <button type="button" class="science" onclick="insertValue('log(')">log</button>
            <button type="button" class="science" onclick="insertValue('pi')">π</button>
            <button type="button" class="science" onclick="insertValue('e')">e</button>
            <button type="button" class="science" onclick="insertValue('**')">^</button>

            <button type="button" class="num" onclick="insertValue('7')">7</button>
            <button type="button" class="num" onclick="insertValue('8')">8</button>
            <button type="button" class="num" onclick="insertValue('9')">9</button>
            <button type="button" class="operator" onclick="insertValue('/')">÷</button>

            <button type="button" class="num" onclick="insertValue('4')">4</button>
            <button type="button" class="num" onclick="insertValue('5')">5</button>
            <button type="button" class="num" onclick="insertValue('6')">6</button>
            <button type="button" class="operator" onclick="insertValue('*')">×</button>

            <button type="button" class="num" onclick="insertValue('1')">1</button>
            <button type="button" class="num" onclick="insertValue('2')">2</button>
            <button type="button" class="num" onclick="insertValue('3')">3</button>
            <button type="button" class="operator" onclick="insertValue('-')">-</button>

            <button type="button" class="num" onclick="insertValue('0')">0</button>
            <button type="button" class="num" onclick="insertValue('.')">.</button>
            <button type="button" class="operator" onclick="insertValue('+')">+</button>
            <button type="button" class="operator" onclick="insertValue('%')">%</button>

            <button type="button" class="clear" onclick="clearDisplay()">C</button>

            <button type="submit" class="equal">=</button>

        </div>
    </form>
</div>

<script>

function insertValue(value){
    document.getElementById("display").value += value;
}

function clearDisplay(){
    document.getElementById("display").value = "";
}

</script>

</body>
</html>
"""

# Allowed functions
allowed = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log10,
    "pi": math.pi,
    "e": math.e,
    "__builtins__": {}
}

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    expression = ""

    if request.method == "POST":

        expression = request.form.get("expression")

        try:
            result = eval(expression, allowed)

        except Exception:
            result = "Invalid Expression"

    return render_template_string(
        HTML,
        result=result,
        expression=expression
    )

if __name__ == "__main__":
    app.run(debug=True)
