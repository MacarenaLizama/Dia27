from flask import Flask, render_template


app=Flask(__name__)

@app.route("/play", methods=['GET'])
def play():
    return render_template('nivel_1.html')

@app.route("/play/<int:x>", methods=['GET'])
def muestra_num_cajas(x):
    return render_template('nivel_2.html',x=x)

@app.route("/play/<int:x>/<string:color>", methods=['GET'])
def colores(x, color):
    return render_template('nivel_3.html', x=x, color=color)

if __name__=="__main__":
    app.run( debug = True, port = 5000)
