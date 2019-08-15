# coding=utf-8
import unittest
import time
import common.HTMLTestRunner_api as HTMLTestRunner_api
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

cur_path = os.path.dirname(os.path.realpath(__file__))   #当前脚本所在文件真实路径



def add_case(caseName="case", rule="test*.py"):
    '''加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建
    if not os.path.exists(case_path): os.mkdir(case_path)
    print('test case path:%s'%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,)
    print(discover)
    return discover

def run_case(all_case, reportName="report"):
    '''执行所有的用例, 并把结果写入测试报告'''
    #now = time.strftime("%Y_%m_%d %H:%M:%s")
    report_path = os.path.join(cur_path,reportName)  #用例文件夹
    if not os.path.exists(report_path):os.mkdir(report_path)
    htmlreport = report_path+r"\result.html"
    print("测试报告生成地址：%s"% htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner_api.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="测试报告",
                                               description="用例执行情况")

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getatime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告：'+lists[-1])
    #找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    '''发送最新的测试报告'''
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg['from'] = sender
    msg['to'] = psw
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    #用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')


if __name__ == "__main__":
    all_case = add_case()     #1加载用例
    #生成测试报告的路径
    run_case(all_case)           #2执行用例
    #获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")          #用例文件夹
    report_file = get_report_file(report_path)        #3获取最新的测试报告
    #邮箱配置
    from config import readConfig
    sender = readConfig.sender
    psw = readConfig.psw
    smtp_server = readConfig.smtp_server
    port = readConfig.port
    receiver = readConfig.receiver
    send_mail(sender, psw, receiver, smtp_server, report_file, port)       #4最后一步发送报告







