import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Get secrets from environment
email_address = os.environ['EMAIL_ADDRESS']
email_password = os.environ['EMAIL_PASSWORD']
to_email = os.environ['TO_EMAIL']

# Read report
with open('reports/latest_report.md', 'r') as f:
    report_content = f.read()

# Create email message
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = to_email
msg['Subject'] = 'DevSecOps Pipeline Report'
msg.attach(MIMEText(report_content, 'plain'))

# Send email via Gmail SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, email_password)
server.send_message(msg)
server.quit()
print("Email sent successfully!")
