# -*- coding: utf-8 -*-
# __author__ = "czw"  1491955388@qq.com
# Date: 2019-10-07  Python: 3.7
import execjs.runtime_names


class WeXin(object):
    """
    爱奇艺 登陆密码解析
    """

    @staticmethod
    def make_pwd(pwd):
        with open("iqiyi_encryption.js", "r", encoding="utf-8") as f:
            ctx = execjs.compile(f.read())

        ret = ctx.call("getpwd", pwd)
        print(ret)


if __name__ == '__main__':
    pdd = WeXin()
    pdd.make_pwd('666666')
