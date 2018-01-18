
"""
初始化时传入全部所需数据，message是正文，可不填，path可以传list或者string；receiver支持多人，用“;”隔开
邮件类。用来给指定用户发送邮件，可指定多个收件人，可带附件。
"""
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from utils.log import logger

class Email:
    #初始化方法
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        """
        初始化Email
        :param server:smtp服务器，必填。
        :param sender: 发件人，必填。
        :param password: 发件人密码，必填。
        :param receiver:收件人，多收件人用"；"隔开，必填。
        :param title: 邮件标题，必填
        :param message:邮件正文，非必填
        :param path:附件路径，可传入list（多附件）或str(单个附件)，非必填。
        """
        self.title = title
        self.message = message
        self.files = path
        self.msg = MIMEMultipart('related')
        self.server = server
        self.sender = sender
        self.receiver = receiver
        self.password = password

    # 附件，非必填
    def _attach_file(self, att_file):
        # 将单个文件添加到附件文件中
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment: filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    # 发送
    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文,非必填
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件(传入list),或者单个附件(传入str)
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)  # 连接server
        except (gaierror and error) as e:
            logger.exception('发送邮件失败，无法连接到SMTP服务器，请检查网络以及SMTP服务器。 %s', e)
        else:
            try:
                smtp_server.login(self.sender,self.password)  #登录
            except smtplib.SMTPAuthenticationError as e:
                logger.exception("用户名密码验证失败! %s", e)
            else:
                # 发送邮件
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            finally:
                smtp_server.quit()   #断开连接
                logger.info('发送邮件"{0}"成功!收件人:{1}。如果没有收到邮件，请检查邮箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))