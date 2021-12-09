import smtplib 
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "abdels6375@gmail.com"
    msg['from'] = user
    password = "FakePassowrdhahahah"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_alert("Hello Wife", "Hello my beautiful, gorgeous, most amazing wifey. I love you so mcuh, and you are my best friend", "wafaosman04@gmail.com")



