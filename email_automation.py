import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, message):
    """
    Sends an email using Gmail's SMTP server.
    """
    # Your Gmail credentials
    from_address = 'debbiecaluya11@gmail.com'  # Replace with your Gmail address
    password = 'uloo vkeg pemk sbah'  # Replace with the App Password

    # Create the email content
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    try:
        # Connect to Gmail's SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_address, password)
            server.sendmail(from_address, to_address, msg.as_string())
        print(f"Email sent successfully to {to_address}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
send_email(
    to_address='debbiecaluya11@gmail.com',  # Replace with the recipient's email
    subject='Hello from Python!',  # Subject of the email
    message='Hi there! This is a test email sent from my Python script. 😊'  # Email body
)
