# 公众号：Python实用宝典
import requests
import json

# 发送
def send_weixin(content):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f302b25c-0d32-403c-985d-c027ba134fce"  # 这里就是群机器人的Webhook地址
    headers = {"Content-Type": "application/json"}  # http数据头，类型为json
    data = {
        "msgtype": "text",
        "text": {
            "content": content,  # 让群机器人发送的消息内容。
            "mentioned_list": [],
        }
    }
    r = requests.post(url, headers=headers, json=data)  # 利用requests库发送post请求



# 读取文件
def read_file(file_name):
    last_site = open('site.txt').read().strip()
    with open(file_name,'r',encoding='utf-8') as f:
        f.seek(int(last_site))
        lines = f.readlines()

        for line in lines[:-1]:
            if line == "\n":
                continue
            try:
                data = json.loads(line)
                last_site = f.tell()
                logical_processing(data)
            except Exception as e:
                print(e)

        site_f = open('site.txt', 'w')
        site_f.write(str(last_site))
        site_f.close()


# 处理逻辑  传一个json数据进来
def logical_processing(alert_json):
    timestamp = alert_json['timestamp']
    alert_level = alert_json['rule']['level']
    ruleid = alert_json['rule']['id']
    description = alert_json['rule']['description']
    agentid = alert_json['agent']['id']
    agentname = alert_json['agent']['name']
    if alert_level >= 12 :
        context = "wazuh-腾讯云告警"+"\n"+ "告警时间："+timestamp +"\n"+"漏洞等级：" + str(alert_level) +"\n"+"规则id："+ ruleid+"\n"+"描述信息："+ description+"\n"+"主机id：" + agentid +"\n"+"主机名字：" + agentname
        print(context)


read_file("alerts.json")
