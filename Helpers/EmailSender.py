from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


def SendEmail(towho, subject, message):
    message = Mail(
        from_email='carrentalapp123@gmail.com',
        to_emails=towho,
        subject=subject,
        html_content=message)
    sg = SendGridAPIClient(api_key=os.getenv("emailkey"))
    sg.send(message)
