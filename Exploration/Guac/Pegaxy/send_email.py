from my_secrets import username, app_password
import smtplib
from email.message import EmailMessage


def email_alert(to, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['to'] = to
    msg['from'] = username

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username, app_password)
    server.send_message(msg)
    server.quit()
