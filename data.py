#coding: utf-8
import socket

#aishowcompany.com 测试用例配置文件
#metinfo 5.3.12


API_IP="47.103.169.26"
API_PORT= 8080

# 测试邮件发送功能case
EMAIL_ADDR='feihongbo1234@163.com'
EMAIL_PASSWD='feihongbo123'

#导入资产
domain_asset = ["test.ai.lakala.cn"]
ip_asset = ["192.168.199.2", "192.168.199.145"]
url_asset = ["http://192.168.1.86/"]    #第一个url资产会添加高级监控

local_ip = socket.gethostbyname(socket.gethostname())

#网站可用性监控
alive_monitor_data = [
    {
        "target": "test.ai.lakala.cn",
        "period": 1,
        "resp_time": 30
    },
    {
        "target": "www.yahoo.com",
        "period": 5,
        "resp_time": 110
    }
]
