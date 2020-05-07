#!./venv/bin/python3.7

import re
import requests
# import sys


def checkIn(username, password):
    new_session = requests.session()

    init_url = "https://hitun.io"
    login_url = " "
    # user_url = "https://hitun.io/user/"
    checkIn_url = "https://hitun.io/user/checkin"

    loginReq_header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }

    loginFrom_data = {
        "email": username,
        "passwd": password
    }

    init_res = new_session.get(init_url)
    if init_res.status_code == 200:
        print("connect success!")
        login_address = re.findall("<a href=\"(.*?)\">.*\n.* 登入", init_res.text)
        login_url = f"{init_url}{login_address[0]}"

    login_res = new_session.post(login_url, headers=loginReq_header, data=loginFrom_data)
    login_str = re.findall(r'\"msg\":\"(.*?)\"', login_res.text)

    if login_str[0].encode('utf-8').decode('unicode_escape') == '欢迎回来':
        checkIn_res = new_session.post(checkIn_url)
        checkIn_str = re.findall(r'\"msg\":\"(.*?)\"', checkIn_res.text)
        # print(checkIn_str)
        message = checkIn_str[0].encode('utf-8').decode('unicode_escape')
        print(message)
    else:
        message = '登录失败，请检查账户信息'

    new_session.close()
    return message
# if __name__ == "__main__":
#     checkIn('qiuzhen11s@163.com', 'QhVm8dqqH3rMkneN'')
