import smtplib, ssl

def send_email(message):
    host="smtp.gmail.com"
    port=465
    # Enter your Email here
    username="example@gmail.com"
    password="App generated password here"
    context=ssl.create_default_context()
    receiver="example@gmail.com"
    with smtplib.SMTP_SSL(host,port, context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
