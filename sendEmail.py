import smtplib, ssl

port = 465
password = 'Heery123!'
context = ssl.create_default_context()

sender_email = "testbambridgewebscraper@gmail.com"
reciever_email = "danielheery@bambridgeaccountants.co.uk"
message = """\
  Subject: Hi Daniel 
  
  This is your test email"""

with smtplib.SMTP_SSL("smtp.gmaiil.com", port, context=context) as server:
  server.login(sender_email, password)
  server.sendmail(sender_email, reciever_email, message)