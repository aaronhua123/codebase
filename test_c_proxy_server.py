import requests


r = requests.get("http://www.baidu.com", proxies={"http":"http://127.0.0.1:8080"})
print(r.text)