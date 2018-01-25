import requests

# B方法，调用了A方法
def visit_taobao():
    return send_request('https://www.taobao.com/')

# A方法
def send_request(url):
    r = requests.get(url)
    return r.status_code
