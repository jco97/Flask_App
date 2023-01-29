from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        height = float(request.form["height"])
        result = "Hi " + name + ", your age is " + str(age) + " and your height is " + str(height) + " meters."
        return render_template("index.html", result=result)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

