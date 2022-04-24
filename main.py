from flask import Flask, render_template, request, redirect, url_for

tasklist = []

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("todo.html", tasklist=tasklist)

@app.route("/add", methods=["POST"])
def receive_data():
    task = request.form["task"]
    tasklist.append(task)
    return redirect(url_for('home'))

@app.route("/delete", methods=["POST"])
def delete():
    tasks = request.form.getlist("tasks")
    for task in tasks:
        tasklist.remove(task)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)