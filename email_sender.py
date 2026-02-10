import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from secrects import sender_email as SENDER_EMAIL, password, receiver_email as RECEIVER_EMAIL


def send_email(receiver_email: str, subject: str, content: str):
    """Send an email to the specified receiver with the given subject and content."""
    # create message
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject

    body = content
    msg.attach(MIMEText(body, "plain"))

    # connect to gmail server (port 465 requires SMTP_SSL)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, password)
        server.send_message(msg)


if __name__ == "__main__":
    send_email(
        receiver_email=RECEIVER_EMAIL,
        subject="Test Email from Python",
        content="Hello Varsha, this email is sent using Python!"
    )
    print("Email sent successfully!")
