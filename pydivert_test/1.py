import requests

# r = requests.get('http://127.0.0.1:5000/')
# print(r.text)
r = requests.get('http://www.baidu.com/')
r.encoding = 'utf-8'
print(r.status_code)
print(r.text)

# 192.168.43.37:? -> 183.2.172.185:80 -> 127.0.0.1:5000
# 127.0.0.1:5000-> 183.2.172.185:80 -> 192.168.43.37:?
#
#