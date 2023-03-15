from flask import Flask,request,render_template , url_for
import re


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def match_regex():
    text_string = request.form["text_string"]
    regular_expression =request.form["regular_expression"]


    matches = re.findall(regular_expression, text_string)

    return render_template("result.html",matches = matches)

#@app.route("/", methods=["GET"])
#def upload(filename):
 #   filename= "http://127.0.0.1:5000/result.html"+filename
  #  return render_template("result.html",filename)

if __name__== "__main__":
    app.run(debug=True)
