import json
from flask import Flask,request, jsonify
from flask_cors import CORS
from otp_send import sendotp
from acubefarms import sendemail
from insert import index

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def hello():
   return ("Application is working Fine")

@app.route('/sendotp',methods=['POST'])
def send_otp():
   return sendotp(request)

@app.route('/acubefarms',methods=['POST'])
def send_email():
   return sendemail(request)

@app.route('/insert',methods=['POST'])
def send_insert():
   return index(request)

if __name__ == "__main__":
  app.run(debug=True)
  #app.run(host="192.168.56.1",port=5000)
 
