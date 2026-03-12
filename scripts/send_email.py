import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Get secrets from environment
email_address = os.environ.get("EMAIL_ADDRESS", "").strip()
email_password = os.environ.get("EMAIL_PASSWORD", "").strip()
to_email = os.environ.get("TO_EMAIL", "").strip()

print(f"Sending report to: {to_email}")  # debug line

if not to_email:
    raise ValueError("TO_EMAIL is empty or not set")

with open("reports/latest_report.md") as f:
    report_content = f.read()

msg = MIMEMultipart()
msg["From"] = email_address
msg["To"] = to_email
msg["Subject"] = "DevSecOps Pipeline Report"

msg.attach(MIMEText(report_content, "plain"))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email_address, email_password)
server.sendmail(email_address, to_email, msg.as_string())
server.quit()

print("Email sent successfully")
