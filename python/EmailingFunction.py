import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "mmohan7755@gmail.com"
receiver_email = "connect2makrant@gmail.com"
subject = "Test Email"
body = "This is a test email from Python."

# Gmail account credentials
email_password = "Monyy$76"

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Establish a connection to the SMTP server (in this case, Gmail)
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # Start TLS for security
    server.starttls()

    # Log in to the email account
    server.login(sender_email, email_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")
