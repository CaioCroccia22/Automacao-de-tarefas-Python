from email.message import EmailMessage
import smtplib
import ssl

password = open('senha.txt', 'r', encoding='UTF-8').read()
from_email = "entendendocuriosidades@gmail.com"
to_email = "entendendocuriosidades@gmail.com"
subject = 'Proposta de parceria'
body = open('corpo.txt', 'r', encoding='utf-8').read()
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
    
    