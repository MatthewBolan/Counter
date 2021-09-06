from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ServerKey'




@app.route('/')
def index():

    if "counter" not in session:

        session["counter"] = 0

    else:

        session["counter"] += 2

    return render_template("index.html")



@app.route('/reset')
def sClear():

        session.clear()

        return redirect ("/")




if __name__ == "__main__":
    app.run(debug=True)