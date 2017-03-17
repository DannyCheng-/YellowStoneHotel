from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = 'menby30122@163.com'
password = '1qazxsw2'
to_addr = 'dycheng@outlook.com'
smtp_server = 'smtp.163.com'
smtp_port = 465

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
