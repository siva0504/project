import json
import smtplib
import psycopg2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendemail(request):

     Name = request.json['Name']
     Email = request.json['Email']
     Phone = request.json['Phone']
     City = request.json['City']
     Message = request.json['Message']

     con = psycopg2.connect(user='uawhauxngssmim',password='2bb78e6924fc159b238fce76bfd2e3efa1b0827cbc99c3dd1fc207ec555d6ae3',host='ec2-79-125-110-209.eu-west-1.compute.amazonaws.com',port='5432',database='d4n8gqnv5nkqri')
     cur = con.cursor()
     sql = "insert into sentiment.acubefarms VALUES ('"+Name+"','"+Email+"',"+str(Phone)+",'"+City+"','"+Message+"')"
     cur.execute(sql)
     con.commit()
     con.close()
     cur.close()
     
     sender = "siva.infocuit@gmail.com"
     receiver = Email
     print(sender,type(sender),receiver,type(receiver))
     
     subject = "booking"
     msg = MIMEMultipart()
     msg['from'] = sender
     msg['to'] = receiver
     msg['subject'] = subject
     # Create the body of the message (a plain-text and an HTML version)
     html = """\
     <html>
      <head></head>
      <body>
        <dl>
        <dt>
    
        <p> <lable><b>Name   :</b><lable><font size="2" color="blue">"""+Name+"""</font></p>
        <p><lable><b>Email   :</b><lable><font size="2" color="blue">"""+Email+"""</font></p>
        <p><lable><b>Phone   :</b><lable><font size="2" color="blue">"""+str(Phone)+"""</font></p>
        <p><lable><b>City    :</b><lable><font size="2" color="blue">"""+City+"""</font></p>
        <p><lable><b>Message :</b><lable><font size="2" color="blue">"""+Message+"""</font></p>
  
        
        </dl>
      </body>
     </html>
     """
     
     #msg.attach(MIMEText(msg['subject'],'plain'))
     msg.attach(MIMEText(html,'html'))
     
     gmailuser = 'siva.infocuit@gmail.com'
     password = 'infocuit'
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     server.login(gmailuser,password)
     text = msg.as_string()
     server.sendmail(sender,receiver,text)
     print ("the message has been sent successfully")
     server.quit()
     return(json.dumps({'Return': 'Message Send Successfully',"Return_Code":"MSS","Status": "Success","Status_Code": "200"}, sort_keys=True, indent=4))
