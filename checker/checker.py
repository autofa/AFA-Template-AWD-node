#!/usr/bin/env python3
# coding=utf-8
# 需引用的模块
import time
import random
import string
import requests
# 出题人使用模块



"""
检测页面与服务可用性的方法，请务必保证公平性
ip: 例如 127.0.0.1
return: 如果检测正常，返回"success"。如果检测异常，请返回异常原因结果，例如"index no access"

注意：
1. 如果需要多个方法，可直接增加方法即可，check()为主方法
2. 每个监测点，请用尽可能详细的备注说明清楚，监测点、原因等等，方便后期运维人员排查


以下check方法为例子，仅供参考
"""
def check(ip):
    # 构建所需url
    url = 'http://' + ip + '/'

    # 基本参数
    timeout=10
    time.sleep(random.randint(1,5))
    

    """
        验证站点首页可用性
    """
    # 确定首页访问正常
    url1 = url+"/xxxxxx/xxxxx.php"
    try:
        res1 = requests.get(url1, timeout=timeout)
    except Exception as e:
        return 'index no access'
    check11 = res1.status_code !=200
    # 确定首页内容显示是否正常
    check12 = '/xxxxxx/xxxxxx.php?m=xxxxxx&c=xxxxxx&a=xxxxxx&xxxxxxxxx=1&uri=' not in res1.text
    if check11 or check12:
        return 'index error' 
    

    """
        验证注册功能是否可用
    """
    header={"Content-Type":"application/x-www-form-urlencoded"}
    s = requests.Session()
    url3 = url+"/xxxxx/xxxxx.php?m=xxxxx&c=xxxxx&a=xxxxx"
    user = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    data = "flag=xxxxxxx&username=%s&xxxxxxx=%s%%40qq.com&xxxxxx=%s&extend_field1=xxxxxxtest&xxxxxx=xxxxxxtest&xxxxxx=xxxxxxtest&xxxxx=xxxxxxtest&xxxxxx=xxxxxxtest&agreement=1&act=acxxxxxt_register&enabled_sms=0&back_act=%%2Fmobile%%2Findex.php%%3Fm%%3Ddefault%%26c%%3Duser%%26a%%3Dindex&Submit=" % (user,user,user)
    try:
        res3 = s.post(url3,data=data,headers=header,timeout=timeout)
    except Exception as e:
        return 'register timeout'
    url4 = url+"/xxxxx/xxxxx.php?m=xxxxxx&c=xxxxxx&a=xxxxxx"
    try:
        res4 = s.get(url4,timeout=timeout)
    except Exception as e:
        return 'login timeout'
    check31 = res4.status_code !=200
    check32 = user not in res4.text
    if check31 or check32:
        return 'login error'


    """
        验证漏洞1. 前台SSRF漏洞页面是否正常可用
    """
    url1 = url+"/xxxxx/?m=xxxxx&c=xxxxx"
    try:
    	res1 = requests.get(url1, timeout=timeout)
    except Exception as e:
        return 'vul1: is no access'


    """
        验证漏洞2. xxxxxxx页面是否正常可用
    """
    url2 = url+"/xxxx/xxx/xxxxxx"
    try:
        res2 = requests.get(url2,timeout=timeout)
    except Exception as e:
        return 'api timeout'
    check21 = res2.status_code !=200
    check22 = 'Authracation has expiried' != res2.text
    if check21 or check22:
        return "api error"

    # 站点运行正常，返回success
    return 'success'


"""
运行程序
"""
if __name__ == "__main__":
    # 出题人使用
    ip = "192.168.1.1"
    print(check(ip))