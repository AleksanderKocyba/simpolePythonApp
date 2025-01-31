from flask import Flask, redirect, url_for
import random

app = Flask(__name__)

@app.route("/")
def home():
    number = random.randint(1, 100)
    return f"""
    <html>
    <head>
        <style>
            body {{
                text-align: center;
                font-family: Arial, sans-serif;
            }}
            .number {{
                font-size: 24px;
                font-weight: bold;
                color: pink;
            }}
            .button {{
                font-size: 18px;
                font-weight: bold;
                color: white;
                background-color: pink;
                border: none;
                padding: 10px 20px;
                margin-top: 20px;
                cursor: pointer;
                border-radius: 10px;
            }}
            .button:hover {{
                background-color: hotpink;
            }}
        </style>
    </head>
    <body>
        <h1 class="number">Wygenerowana liczba: {number}</h1>
        <form action="/reload">
            <button class="button" type="submit">Generuj nową liczbę</button>
        </form>
    </body>
    </html>
    """

@app.route("/reload")
def reload():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
