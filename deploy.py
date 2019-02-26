from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/graphicDesign")
def graphicDesign():
    return render_template("graphicDesign.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")
    
if __name__ == "__main__":
    app.run(debug=True)