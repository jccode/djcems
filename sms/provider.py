# -*- coding:utf-8 -*-

import urllib2, urllib, string, random, logging
import xmltodict
from django.conf import settings


logger = logging.getLogger(__name__)

class HuYiSms:
    post_url = 'http://106.ihuyi.cn/webservice/sms.php?method=Submit'
    identifier = 'huyi'
    template = "您的验证码是：{code}。请不要把验证码泄露给其他人。"

    def __init__(self):
        conf = settings.SMS
        self.username = conf[self.identifier]['username']
        self.password = conf[self.identifier]['password']

    def random_digits(self, length):
        return ''.join(random.sample(string.digits * (length / 10 + 1), length))

    def send(self, mobile):
        code = self.random_digits(6)
        post_data = [
            ("account", self.username),
            ("password", self.password),
            ("mobile", mobile),
            ("content", self.template.format(code=code)),
        ]
        result = urllib2.urlopen(self.post_url, urllib.urlencode(post_data))
        content = result.read()
        print(content)
        # check result
        ret = xmltodict.parse(content)['SubmitResult']
        print(ret)
        if ret['code'] == '2':
            logger.info("send message success. The code is %s" % ret['code'])
            return code
        else:
            logger.error("send message failed. error code: %s, error: %s" % (ret['code'], ret['msg']))
            return 0






