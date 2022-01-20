import re
import urllib.request
import urllib.response
import time
try:
    import requests
except:
    import os
    os.system("pip3 install  -i https://pypi.tuna.tsinghua.edu.cn/simple requests")
    import requests


__head={r"user-agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
def openURL(url:str)->str:
    """    request=urllib.request.Request(url,headers=_head,\
        origin_req_host="https://www.runoob.com/python3/python-urllib.html")
    time.sleep(0.1)
    reponse = urllib.request.urlopen(request).read()
    try:
        dst=reponse.decode('utf-8')
    except:
        dst=reponse.decode('GB2312')"""
    return requests.get(url,headers=__head).text
class Item:
        def __init__(self,title,link) -> None:
            self.link=link
            self.title=title
            self.content=None
            self.ignore=False
def write(text:str,name:str)->None:
    f=open(name+(".txt"),"w",encoding='utf-8')
    f.write(text)
    f.close()
bookName=""