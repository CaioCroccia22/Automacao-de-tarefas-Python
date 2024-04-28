from email.message import EmailMessage
import smtplib
import ssl

password = open('senha.txt', 'r').read()
# print(password)

# email de envio
from_email = "entendendocuriosidades@gmail.com"

# email que vai estar recebendo
to_email = "entendendocuriosidades@gmail.com"

subject = "Curso Python"

body = '''
Melhor forme de prever o futuro é cria - lo
linguagem python


'''

# 1 - estruturando a messangem de email

message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)

# Criando o contexto via SSL

safe = ssl.create_default_context()

# Envio do email (servidor, porta, context)
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    # Fazer login
    smtp.login(from_email, password)
    
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )
