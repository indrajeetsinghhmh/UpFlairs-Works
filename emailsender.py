import smtplib

email = input("SENDER EMAIL: ")
recieverMail = input("RECIEVER EMAIL: ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "xlbi yryr mqnh pkpt")

server.sendmail(email, recieverMail, text)

print("Email has been sent to " + recieverMail)