from flask import Flask,request
app = Flask(__name__)
@app.route("/",methods=['POST'])
def index():
    return "hello world"
    
