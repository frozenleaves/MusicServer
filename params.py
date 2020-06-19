# -*- coding: utf-8 -*-

import urllib.parse
import requests
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

SOURCE_FLAG = False

def search_result(name, flag=False):
    if flag:
        global SOURCE_FLAG
        SOURCE_FLAG = True
    url = 'https://api.zhuolin.wang/api.php?callback=jQuery11130961330207846312_1591435825529&types=search&count=100&source=netease&pages=1&name={search_name}'.format(
        search_name=urllib.parse.quote(name))
    url2 = 'https://api.zhuolin.wang/api.php?callback=jQuery111307658118632618403_1591936704692&types=search&count=100&source=kugou&pages=1&name={search_name}'.format(
        search_name=urllib.parse.quote(name))
    if SOURCE_FLAG:
        response = requests.get(url, headers=headers)
        result = re.match(r"jQuery11130961330207846312_1591435825529\((\[.*\])\)", response.text)
    else:
        response = requests.get(url2, headers=headers)
        result = re.match(r"jQuery111307658118632618403_1591936704692\((\[.*\])\)", response.text)
    print(type(json.loads(result.group(1))))
    tmp_ret = json.loads(result.group(1))
    for i in tmp_ret:
        if i.get("name") != name:
            tmp_ret.remove(i)
    return tmp_ret


def get_target_file_url(id):
    if SOURCE_FLAG:
        source_url = 'https://api.zhuolin.wang/api.php?callback=jQuery11130961330207846312_1591435825529&types=url&id={_id}'.format(
        _id=id)
    else:
        source_url = 'https://api.zhuolin.wang/api.php?callback=jQuery111307658118632618403_1591936704692&types=url&id={_id}&source=kugou'.format(
        _id=id)
    resp1 = requests.get(source_url, headers=headers)
    if SOURCE_FLAG:
        result = re.match(r"jQuery11130961330207846312_1591435825529\(({.*\})\)", resp1.text)
    else:
        result = re.match(r"jQuery111307658118632618403_1591936704692\(({.*\})\)", resp1.text)
    file_url = json.loads(result.group(1)).get("url")
    return file_url


def download(url, file_name):
    resp2 = requests.get(url=url, headers=headers)
    with open('./static/tmp/' + file_name , 'wb') as f:
        f.write(resp2.content)
    return True


if __name__ == '__main__':
    import os

    print(os.getcwd())
