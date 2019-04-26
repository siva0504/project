import json
from flask import Flask,request, jsonify
from flask_cors import CORS
from Inserttwilioreservation import Inserttwilioreservation
#----------translator-----------#
from translator import translatortamil
#---------------------------------------------------
from botinsert import fun
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def hello():
   return ("Hello Twilio")

@app.route('/send_OTP',methods=['GET','POST'])
def indexotp():
   return index(request)

if __name__ == "__main__":
  app.run(debug=True)
  #app.run(host="192.168.1.29",port=5000)
