from flask import Flask,request
import urllib
import psycopg2
import random
import json

def sendotp(request):
    mobile = request.json['mobile']
    authkey_msg91 = '195833ANU0xiap5a708d1f'
    c = random.randint(0,99999999)
    print(c)
    otp_generate = str(c)
    
    url = 'http://control.msg91.com/api/sendotp.php?&authkey='+authkey_msg91+'&message=Your verification code is '+otp_generate+'&sender=OTPSMS&mobile='+mobile+'&otp='+otp_generate

    print(url)
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
       test = str(the_page)
       test = test[2:-1]
       test = json.loads(test)
    return json.dumps([(test)])
    


   
