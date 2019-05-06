from flask import Flask,request
import psycopg2
import json
def index(request):
     email = request.json['email']
     dob = request.json['dob']
     mobile = request.json['mobile']
     con = psycopg2.connect(user='uawhauxngssmim',password='2bb78e6924fc159b238fce76bfd2e3efa1b0827cbc99c3dd1fc207ec555d6ae3',host='ec2-79-125-110-209.eu-west-1.compute.amazonaws.com',port='5432',database='d4n8gqnv5nkqri')
     cur = con.cursor()
     sql = "insert into sentiment.leader VALUES ('"+email+"', '"+dob+"','"+mobile+"')"
     cur.execute(sql)
     con.commit()
     return(json.dumps({'Status': 'Success','Message': 'Data Insert Sucessfully'},indent=4))
     con.close()
     cur.close()

