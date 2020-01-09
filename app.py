## Sean Landry
from flask import Flask, request
from flask.logging import default_handler
import smtplib
import json
import os
import logging
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

root = logging.getLogger()
root.addHandler(default_handler)
root.setLevel(logging.INFO)

## setup flask app
app = Flask(__name__)
app.logger.setLevel(logging.INFO)

def sending_email(request, method, remote_addr):
    app.logger.info("sending email notification to " + str(os.environ["RECIEVER_EMAIL"]))
    port = os.environ.get("ISMTP_PORT", 25)
    ## example relay 'ismtp.gmail.com'
    relay = os.environ["ISMTP_RELAY"]

    subject = method + " recieved"
    body = "Remote address: \n" + remote_addr + "\nThe request json: \n" + json.dumps(request, indent = 2, sort_keys = True)
    sender_email = os.environ.get("SENDER_EMAIL", "dev@rest-minimal.com")
    receiver_email = os.environ["RECIEVER_EMAIL"]

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()
    with smtplib.SMTP(relay, port) as server:
        server.sendmail(sender_email, receiver_email, text)


@app.route('/', methods=['GET', 'POST'])
def basic():
    app.logger.info("recieved " + request.method + " from " + request.remote_addr + "\n" + json.dumps(request.json, indent = 2, sort_keys = True))
    if request.json:
        return request.json, 200
    else:
        return "hello world", 200

@app.route('/send_email/', methods=['GET', 'POST'])
def send_email():
    app.logger.info("recieved " + request.method + " from " + request.remote_addr + "\n" + json.dumps(request.json, indent = 2, sort_keys = True))
    if request.json:
        sending_email(request.json, request.method, request.remote_addr)
        return request.json, 200
    else:
        sending_email("hello world", request.method, request.remote_addr)
        return "hello world", 200




if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')
