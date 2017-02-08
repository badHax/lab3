import smtplib

from_name = "Bob"
to_name = "Tom"
subject = "Random Thoughts"
msg = "Greeting human,\n\nWhere do dogs go when they die?"
from_addr = '*******dz@gmail.com'
to_addr = '*******dz@gmail.com'
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name,
 to_addr, subject, msg)
# Credentials (if needed)
username = '********dz@gmail.com'
password = '****************'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 