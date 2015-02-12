import smtplib

fromaddr = 'nostaw7@gmail.com'
fromname = 'Alex Watson'
toaddr  = 'nostaw7@gmail.com'
toname = 'me'
subject = "test mail"
msg = "this is a test email from my nitrous setup"

message = """From: {} <{}>
To: {} <{}>
Subject: {} 
 {} 
"""
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)


# Credentials (if needed)
username = 'nostaw7@gmail.com'
password = 'not putting that out there'


# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()
