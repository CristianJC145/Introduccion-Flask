from smtplib import SMTP #importar de la libreria smtplib SMTP, servidor de correos
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('Este es un mensaje de prueba')

msg['Subject'] = 'Austo de prueba'
msg['From']= 'cristianjamioy2020@itp.edu.co'
msg['To']='cristianjamioy2020@itp.edu.co'

username = 'cristianjamioy2020@itp.edu.co' #correo de gmail y contraseña
password ='1006843635'

server = SMTP('smtp.gmail.com:587') #url en la cual se encuetra el servidor de correos
server.starttls() #habilitar protocolo seguro de correos
server.login(username, password) #logueo
server.send_message(msg) #enviar correo, a quien, de donde y mensaje

server.quit() #cerrar