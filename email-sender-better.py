import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())


email = EmailMessage()
email['from'] = 'revaoli'
email['to'] = 'revamunish@gmail.com'
email['subject'] = 'this is a test email being sent thru python script'

email.set_content(html.substitute({'name': 'John', 'last_name' : 'Doe'}), 'html')

with smtplib.SMTP('smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('reva12munish@gmail.com','ufqtrwjvmysqtlkv') #app password needs to be generated from google 
    smtp.send_message(email)
    print('all done ✌🏻')