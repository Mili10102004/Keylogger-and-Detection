import smtplib
from email.mime.text import MIMEText
import ssl

EMAIL_ADDRESS = "ahadshaikh1504@gmail.com"
EMAIL_PASSWORD = "xkmz cshj ogsp kskv"

message = MIMEText("Test email")
message["Subject"] = "Test Email"
message["From"] = EMAIL_ADDRESS
message["To"] = EMAIL_ADDRESS

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message.as_string())
    print("Test email sent successfully!")
except Exception as e:
    print(f"Error sending test email: {e}")
