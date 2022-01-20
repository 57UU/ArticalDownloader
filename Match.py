
import re
import Net
#setting
isTitleContainBookName=True
isDebug=True
try:
    from lxml import etree
except:
    import os
    os.system("pip3 install  -i https://pypi.tuna.tsinghua.edu.cn/simple lxml")
    from lxml import etree
isDebug=isDebug



def verify(text:str)->str:
    isMatch=False
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':
            isMatch=True
            break
    if(isMatch):
        return text
    return ""    
    
p=re.compile("<a.+?>.+?<\/a>")
def removeLink(text:str)->str:
    t=p.sub("",text,count=10000)
    return t
regular_divs=["content","chapter_content","booktext"]
def findDiv(text:str,key:str)->str:
    tree=etree.HTML(text)
    html_data = tree.xpath('//div[@id="%s"]/text()'%key)
    data=""
    for i in html_data:
        data+=verify(i)
    return data

p2=re.compile(r'<div.*?id="(.+?)".*?>(.|\s)*?<\/??div')
def getDivs(text):
    #print("Text->",text)
    tep=p2.findall(text)
    tep2=[i[0] for i in tep]
    return tep2

p3=re.compile(r"<.?title.?>(.+?)<.?/.?title.?>")
def getTitle(text:str)->str:
    return p3.search(text).group(1)

junks=["&nbsp;"," "]
p4=re.compile("<.?br.*?>")
def clear(text:str):
    for junk in junks:
        text=text.replace(junk,"")
    text= p4.sub("",text,100000)
    d=""
    for i in text:
        if(i.isprintable()):
            d+=i
    return d

regular=re.compile(">.+?<")
def findContent(string:str,item:Net.Item)->str:
    global isDebug
    #print("finding: ",string)

    if(isTitleContainBookName):
        title=getTitle(string)
        print(item.title,'->',title)
        if title.find(Net.bookName)==-1:
            item.ignore=True
            return None
    if isDebug:
        isDebug=True
        Net.write(string,"debug")
    
    #string=regular1.search(string).group(1)
    #string=string.replace(" ","")
    #string=removeLink(string)
    list=getDivs(string)
    key=None
    for i in list:
        if key==None:
            name:str=i.lower()
            for keyword in regular_divs:
                if keyword in name:
                    key=i
                    break
    if(key==None):
        print("Can't find Key")
        item.ignore=True
        return ""
    dst=findDiv(string,key)
    dst=clear(dst)
    """
    l=regular.findall((string))
    dst=""
    for i in l:
        dst+=verify(i)
        """
    return dst