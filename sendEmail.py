import smtplib

HOST = "smtp.mydomain.com"
SUBJECT = "Happy Holidays"
TO = "mirurated@gmail.com"
FROM = "okenyebrian@gmail.com"
text = "Have a nice holiday Mr."
BODY = "\r\n".join((
    f"From:{FROM}",
    f"To:{TO}",
    f"Subject:{SUBJECT}",
    "",
    text
))
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()
