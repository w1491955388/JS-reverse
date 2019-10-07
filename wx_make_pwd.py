# -*- coding: utf-8 -*-
# __author__ = "czw"  1491955388@qq.com
# Date: 2019-10-07  Python: 3.7
import execjs.runtime_names


class WeXinGZH(object):
    """
    微信公众号 登陆密码加密
    """

    @staticmethod
    def get_pwd(pwd):
        with open("wx_encryption.js", "r", encoding="utf-8") as f:
            ctx = execjs.compile(f.read())

        ret = ctx.call("getpwd", pwd)
        print(ret)


if __name__ == '__main__':
    pwd = WeXinGZH()
    pwd.get_pwd('666666')
