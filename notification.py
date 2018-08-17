server = 'email-smtp.us-east-1.amazonaws.com'
user = 'AKIAJKEPOAWWFMV5IJ7A'
password = 'AkrtB6gWnOFBAM+TNqN3DHdZPhUjeqIUTimuwzttO1if'

import smtplib
server = smtplib.SMTP(server, 587)
server.login(user, password)

msg = 'Hi it works'
server.sendmail("shailendra", "target@example.com", msg)