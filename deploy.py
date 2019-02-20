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

@app.route("/gitHub")
def gitHub():
    return render_template("gitHub.html")

@app.route("/javaScriptProjects")
def javaScriptProjects():
    return render_template("javaScriptProjects.html")
    
if __name__ == "__main__":
    app.run(debug=True)