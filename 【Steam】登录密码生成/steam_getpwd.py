# -*- coding: utf-8 -*-
# __author__ = "czw"  1491955388@qq.com
# Date: 2019-10-07  Python: 3.7
import time
import json
import requests
import execjs.runtime_names


class Steam(object):
    """
    Steam 登陆密码解析
    """
    @staticmethod
    def get_parameter():
        url = 'https://store.steampowered.com/login/getrsakey/'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }

        data = {
            'donotcache': lambda: int(round(time.time() * 1000)),  # 获取十三位时间戳
            'username': '13888888888'  # 登录账号
        }

        resp = requests.post(url, headers=headers, data=data)
        html = json.loads(resp.text)
        publickey_mod = html['publickey_mod']
        publickey_exp = html['publickey_exp']
        return publickey_mod, publickey_exp

    @staticmethod
    def get_pwd(pwd, publickey_mod, publickey_exp):
        with open("steam_encrption.js", "r", encoding="utf-8") as f:
            ctx = execjs.compile(f.read())

        ret = ctx.call("getpwd", pwd, publickey_mod, publickey_exp)
        print(ret)


if __name__ == '__main__':
    parameter = Steam.get_parameter()
    Steam.get_pwd('666666', parameter[0], parameter[1])
