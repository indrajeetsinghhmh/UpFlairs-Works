import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Email details
    sender_email = "kuldeepraika64@gmail.com"
    sender_password = "kuldeepsingh0123"
    receiver_email = "ranjit.upflairs@gmail.com"

    # Email content
    subject = "Student Details"
    body = """
    Name: Your Name
    Year: Your Year
    Branch: Your Branch
    College: Your College
    """


    # Setting up the MIME
    msg = MIMEMultipart()
    msg['From'] = indrajeet.business01@gmail.com
    msg['To'] = ranjit.upflairs@gmail.com
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    msg.

    try:
        # Create SMTP session for sending the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable security
            server.login(indrajeet.business01@gmail.com, kuldeepsingh0123)  # Login with sender's email and password
            text = msg.as_string()
            server.sendmail(indrajeet.business01@gmail.com, ranjit.upflairs@gmail.com, text)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
    send_email()