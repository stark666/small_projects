#coding=gbk
import requests
import re
from PIL import Image


# ���� Request headers
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'

headers = {
    "User-Agent": agent,
    "Host": "weibo.cn",
    "Origin": "https://login.weibo.cn",
    "Referer": "https://login.weibo.cn/login/"
}

session = requests.session()

url_login = 'https://weibo.cn/login/'


def get_params(url_login):
    html = session.get(url_login, headers=headers)
    # print(html.text)
    pattern = r'action="(*?)".*?type="password" name="(.*?)".*?name="vk"\value="(.*?)".*?name="capId" value="(.*?)"'
    res = re.findall(pattern, html.text, re.S)
    # print(res)
    return res


def get_cha(capId):
    cha_url = "http://weibo.cn/interface/f/ttt/captcha/show.php?cpt="
    cha_url = cha_url + capId
    cha = session.get(cha_url, headers=headers)
    with open('cha.jpg', 'wb') as f:
        f.write(cha.content)
        f.close()
    try:
        im = Image.open('cha.jpg')
        im.show()
        im.close()
    except:
        print("�뵽��ǰĿ��ȥ��cha.jpg ������֤��")
    cha_code = input("��������֤��:")

    return cha_code


res = get_params(url_login)
print res
if res == []:
    print("������������⣬�������������")
else:
    post_url, password, vk, capId = res[0]


if __name__ == "__main__":
    cha_code = get_cha(capId)
    email = raw_input("��������������˺Ż����ֻ�����:")
    password_input = raw_input("�������������:")
    postdata = {
        "mobile": email,
        "code": cha_code,
        "remember": "on",
        "backURL": "http%3A%2F%2Fweibo.cn",
        "backTitle": "΢��",
        "tryCount": "",
        "vk": vk,
        "capId": capId,
        "submit": "��¼",
    }
    # print(postdata)
    postdata[password] = password_input
    post_url = url_login + post_url
    # print(post_url)
    page = session.post(post_url, data=postdata, headers=headers)
    index = session.get("http://weibo.cn")
    print(index.text)
    # cookies = requests.utils.dict_from_cookiejar(session.cookies)
    # print(cookies)