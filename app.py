from flask import Flask, render_template

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/peso")
def peso():
    return render_template("peso.html")

@app.route("/altura")
def altura():
    return render_template("altura.html")

if __name__ == "__main__":
    app.run(debug=True)