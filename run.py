# -*- coding: utf-8 -*-
import time, os
import unittest, requests
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from email.mime.multipart import MIMEMultipart
from main import MyTestCase


class RunTest:
    def __init__(self):
        self.filename = ''
        pass

    def test_report(self):
        test_dir = os.getcwd() + r'\testReport'
        # 运行类下面的test所有用例
        #suite = unittest.makeSuite(MyTestCase)

        # 构造测试集
        suite = unittest.TestSuite()
        suite.addTest(MyTestCase("test_customer"))
        suite.addTest(MyTestCase("test_supplier"))
        suite.addTest(MyTestCase("test_newproduct"))
        suite.addTest(MyTestCase("test_othersinto"))
        suite.addTest(MyTestCase("test_warehouses"))

        # 执行测试
        runner = unittest.TextTestRunner()


        # 运行当前目录下，以test开头的所有用例
        # suite = unittest.defaultTestLoader.discover('.', 'test*.py')
        print(suite)
        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        self.filename = test_dir + '/' + now + 'test_result.html'
        fp = open(self.filename, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"接口测试报告", description=u"测试用例执行情况：")
        runner.run(suite)
        fp.close()


    def mail_test(self):
        # 发件人和收件人
        sender = 'xie.zl@ikcrm.com'
        receiver = '575631668@qq.com', 'jiang.hw@ikcrm.com', 'yu.zx@ikcrm.com'  # 'xiezhilin745@163.com'

        # 所使用的用来发送邮件的SMTP服务器
        smtpserver = 'smtp.exmail.qq.com'
        # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
        username = 'xie.zl@ikcrm.com'
        password = 'PK6TTNztP2bE6Huo'

        # 邮件主题
        mail_title = '进销存接口自动化测试报告' + time.strftime("%Y-%m-%d")

        # 读取html文件内容
        f = open(self.filename, 'rb')  # HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
        mail_body = f.read()
        # print(mail_body)
        f.close()

        # 初始化邮件
        message = MIMEMultipart()

        # 邮件内容, 格式, 编码
        html_repote = MIMEText(mail_body, 'html', 'utf-8')
        message.attach(html_repote)
        # 邮件附件和header
        html_att = MIMEApplication(open(self.filename, 'rb').read())
        html_att.add_header('Content-Disposition', 'attachment', filename="test_result.html")
        message.attach(html_att)

        message['From'] = sender  # Header('谢芝林','utf-8')
        # message['To'] = receiver   #这样只能发一个人
        message['To'] = ','.join(receiver)  # 这样可以发送给多人
        message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)  # SMTP服务器
            smtp.login(username, password)  # 用户名和授权码
            smtp.sendmail(sender, receiver, message.as_string())  # 发送邮件
            print("发送邮件成功！！！")
            smtp.quit()
        except smtplib.SMTPException:
            print("发送邮件失败！！！")


if __name__ == '__main__':
    rt = RunTest()
    rt.test_report()
    #rt.mail_test()
    # rt.test_email(subject,msg,to_addrs,from_addr,smtp_addr,password)
