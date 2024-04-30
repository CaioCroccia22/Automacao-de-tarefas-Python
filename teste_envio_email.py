  
#   Teste outros metodos 
  
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# # Configurações de autenticação
# email_sender = "entendendocuriosidades@gmail.com"
# email_password = 'teste12345*'

# # Configurações do servidor SMTP do Gmail
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587

# # Criar mensagem de e-mail
# msg = MIMEMultipart()
# msg['From'] = email_sender
# msg['To'] = 'destinatario@example.com'
# msg['Subject'] = 'Assunto do e-mail'

# # Corpo do e-mail
# body = 'Corpo do e-mail.'
# msg.attach(MIMEText(body, 'plain'))

# # Autenticar e enviar e-mail
# try:
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
#     server.login(email_sender, email_password)
#     text = msg.as_string()
#     server.sendmail(email_sender, 'destinatario@example.com', text)
#     print('E-mail enviado com sucesso!')
# except Exception as e:
#     print('Erro ao enviar e-mail:', str(e))
# finally:
#     server.quit()