import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# sender details
sender_email = "varsh6362@gmail.com"
receiver_email = "ssonuprakashks@gmail.com"
password = "rydj tome vhdd ockp"

# create message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Test Email from Python"

body = "Hello Varsha, this email is sent using Python!"
msg.attach(MIMEText(body, "plain"))

# connect to gmail server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# login
server.login(sender_email, password)

# send email
server.send_message(msg)

print("Email sent successfully!")

server.quit()
