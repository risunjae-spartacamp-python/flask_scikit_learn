from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calc", methods=["POST"])
def calc():
    request.form["calc"]
    with open("predict_population.pickle", mode="rb")as fp:
    model = pickle.load(fp)
    resul t= model.predict(np.array([[1300000]]))
    return render_template("calc.html")


if __name__ == "__main__":
    app.run(debug=True)
