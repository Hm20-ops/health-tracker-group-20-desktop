import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QMessageBox

'''
A helper function to display message box when an error occurs or 
give success information to user
'''
def display_message(title, text, error=True):
    msg = QMessageBox()
    msg_type = QMessageBox.Critical if error else QMessageBox.Information
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(msg_type)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

'''
A helper function to send email to an email address, that is used for when creating account 
and invite a user to a group and notify group members of archiving group goal or a new group goal
'''
def send_email_to(email_to, title, message_text):
    email = 'emailforadvertsandtests@gmail.com'
    password = 'doonrkovjqdmmqow'
    send_to_email = email_to
    subject = title  # The subject line
    message = message_text

    # creating the email instance(MIMEMultipart) and set header fields
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    # Attach the message to the email object
    msg.attach(MIMEText(message, 'plain'))

    # Login to the email server with TLS and send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()  # convert the email object to a string to send
    server.sendmail(email, send_to_email, text)
    server.quit()