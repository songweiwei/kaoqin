from email.mime.text import MIMEText  #纯文本，HTML
from email.mime.image import MIMEImage #图片
from email.mime.multipart import MIMEMultipart #多种组合内容

# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header
import traceback

class sendEmail():
    def __init__(self,from_addr,from_name,from_password,to_addr,to_name,smtp_server):
        self.from_addr=from_addr
        self.from_name=from_name
        self.from_password=from_password
        self.to_addr=to_addr
        self.to_name=to_name
        self.smtp_server=smtp_server
        self.smtpobj = smtplib.SMTP_SSL(self.smtp_server)

    def log_in(self):
        # 建立连接--qq邮箱服务和端口号（可百度查询）
        self.smtpobj.connect(self.smtp_server, 465)
        # 登录--发送者账号和口令
        self.smtpobj.login(self.from_addr, self.from_password)

    def send_msg(self,subject,message):
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = Header(self.from_name)  # 发送者
        msg['To'] = Header(self.to_name)  # 接收者
        msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题
        self.smtpobj.sendmail(self.from_addr, self.to_addr, msg.as_string())

    def close(self):
        self.smtpobj.quit()


