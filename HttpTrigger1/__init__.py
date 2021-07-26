import logging
import azure.functions as func
import sendgrid
import os
from sendgrid.helpers.mail import *
from html import escape

# REFERENCE: https://github.com/sendgrid/sendgrid-python

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get & validate parameters
    to=get_param(req, "to")
    if not to:
        return func.HttpResponse("Missing required parameter 'to'.", status_code=400)
    logging.info(f"Email to: {to}")

    subject=get_param(req, "subject")
    if not subject:
        return func.HttpResponse("Missing required parameter 'subject'.", status_code=400)
    logging.info(f"Email subject: {subject}")

    emailFrom=os.environ.get('EMAIL_FROM')
    logging.info(f"Email from: {emailFrom}")

    # Call SendGrid API
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    mail = Mail(Email(emailFrom), To(to), Subject(subject), Content("text/plain", "Email sent from Azure Function."))

    response = sg.client.mail.send.post(request_body=mail.get())

    logging.info(f"Sendgrid response code: {response.status_code}")
    #logging.info(f"Sendgrid response body: {response.body}")
    #logging.info(f"Sendgrid response headers: {response.headers}")

    return func.HttpResponse(f"Email sent to {escape(to)} with subject {escape(subject)}. Sendgrid response code: {response.status_code}.", status_code=200)

def get_param(req: func.HttpRequest, param: str) -> str:
    # Check for querystring parameter (GET)
    val=req.params.get(param)

    # If not in querystring, check in POST JSON body
    if not val:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            val = req_body.get(param)

    return val
