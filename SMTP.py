import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpServer='smtp.163.com'

#你的用户名和密码
user=''
password=''

#发送邮箱
sender='ss@163.com'
#接受邮箱
receive='bb@126.com'

#邮件标题
subject='Web Selenium 自动化测试报告'
#内容
content='<html><h1 style="color:red">加油！学习使人有动力</h1></html>'
#内容装载，防止乱码用utf-8
msg=MIMEText(content,'html','utf-8')
#标题装载，S大写
msg['Subject']=Header(subject,'utf-8')
#发送方装载，要重新写邮箱
msg['From']='ss@163.com'
msg['To']='bb@126.com'
#方式和端口,SSL登录安全
smtp=smtplib.SMTP_SSL(smtpServer,465)
#认证
smtp.helo(smtpServer)
smtp.ehlo(smtpServer)
#登录
smtp.login(user,password)

print("Start send Email...")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("Send Email end")