import smtplib
from utils.config import get_config

config = get_config()

class Email:

    def __init__(self):
        self.email_id = config["EMAIL_OWNER"]
        self.password = config["EMAIL_PASS"]

    def send_email(self, subject: str | None = None, body: str | None = None):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email_id,password=self.password)
            connection.sendmail(from_addr=self.email_id, to_addrs=self.email_id, msg=f"subject: {subject}\n\n{body}")
