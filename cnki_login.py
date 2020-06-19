# -*- coding: utf-8 -*-

import requests
import time

login_url = 'http://auth.wit.edu.cn/authserver/login?service=https%3A%2F%2Fidp.wit.edu.cn%2Fidp%2FAuthn%2FExtCas%3Fconversation%3De1s1&entityId=https%3A%2F%2Ffsso.cnki.net%2Fshibboleth'

headers = {
    'Host': 'auth.wit.edu.cn',
    'Connection': 'keep-alive',
    'Content-Length': '176',
    # [Content length: 176]
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://auth.wit.edu.cn',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://auth.wit.edu.cn/authserver/login?service=https%3A%2F%2Fidp.wit.edu.cn%2Fidp%2FAuthn%2FExtCas%3Fconversation%3De1s1&entityId=https%3A%2F%2Ffsso.cnki.net%2Fshibboleth',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

# cookies = {
#     'JSESSIONID_ids2': '0001dEXA2rpQNujMiF1DLA7JKU9:19pk4b0hp',
#     'JSESSIONID-WYYY': '5duUnQzCoeZXC0p%2FDD3zq%2BMpznz55YZl4Pu1hMjF%2FMXIfd%2FHF%2BFg%2FoDZwxpvzYPfl0pArRzC4Ry74%2ByKR9Rf1xdIGZP3sQZgBp9WNwvUodSdqUF9ec4R%2F59wKF%5CiAlyWhAGYPUXEcWMER%2BJncaaRupE1JZBAap2xHcj6HSTXSibUCsMg%',
#     'iuqxldmzr': '32',
#     'Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c': '%d' % round(time.time()),
#     'Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c': '%d' % round(time.time())
#
# }

post_data = {
    "username": "1706240308",
    "password": "cx2414672604",
    "lt": "LT-1855426-RgHt7YFGmof2fQ0Q9bOgnnSF3cjDsX1591697966835-bvwB-cas",
    "dllt": "userNamePasswordLogin",
    "execution": "e1s1",
    "_eventId": "submit"

}

index_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',

}

session = requests.Session()

response = session.post(url=login_url, headers=headers)
#
index_url = 'https://www.cnki.net/'

resp = session.get(index_url, headers=index_headers)

print(resp.content.decode('utf-8'))
