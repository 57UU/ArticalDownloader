import Net
import re
import Match












url="https://www.rizhaoxs.com/b/23/23036/"

prefix=re.search(r"(https?://.+?)/",url).group(1)
print("mother web:",prefix)
html=Net.openURL(url)
bookName=re.search(r"<.?title.?>(.+?)<.?/.?title.?>",html).group(1)[:3]
print("Book name:",bookName)
Net.bookName=bookName
Net.write(html,"index")

start=re.search("正文|全部",html)
if start!=None:
    html=html[start.end():]
identify=re.compile(r'<a href.?=\"(.+?)\">(.+?)</a>')
all=[]
for i in identify.findall(html):
    link=i[0]
    title:str=i[1]

    if link.find("http")==-1:
            link2=prefix+link
    else:
        link2=link
    all.append(Net.Item(title,link2))
f=open("download.txt","w",encoding='utf-8')
for i in all:
    i.content=Match.findContent(Net.openURL(i.link),i)
    if(i.ignore or i.content==None):
        continue
    print("Content->",i.content)
    f.write(i.title+'\n')
    f.write(i.content)
    f.flush()
f.close()

