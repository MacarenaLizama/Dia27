from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def mostrar_tablero():
    num1=4
    return render_template("index_1.html", num1=num1)

@app.route("/4", methods=['GET'])
def mostrar_tablero_4():
    num1=2
    return render_template("index_2.html", num1=num1)

@app.route("/<int:x>/<int:y>", methods=['GET'])
def mostrar_tablero_xy(x,y):
    return render_template("index_3.html", x=x, y=y)

if __name__=="__main__":
    app.run(debug=True, port=5001)