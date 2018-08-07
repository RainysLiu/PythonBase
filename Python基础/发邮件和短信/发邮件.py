
import smtplib
from email.mime.text import MIMEText
SMTPServer='smtp.163.com'
Sender='Rainys_Liu@163.com'
PassWord='123456a'
message= "优点：简单、易学、免费且开源、高层语言、可移植性强、具有解释性、面向对象语言、具有可扩展性、代码规范" \
        "缺点：运行速度慢、国内市场小、中文资料少、构架选择较多" \
        "应用场景：web开发、OS管理、服务器运维的自动化脚本、科学计算、桌面软件、网络服务器软件、游戏、产品早期原型和迭代"
mesg=MIMEText(message)
mesg['Subject']='关于学习python的知识要点'
mesg['From']=Sender
mailServer=smtplib.SMTP(SMTPServer,25)
mailServer.login(Sender,PassWord)
mailServer.sendmail(Sender,['Rainys_Liu@163.com','xuechangan1126@163.com'],mesg.as_string())
mailServer.quit()



