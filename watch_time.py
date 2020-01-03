from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import timedelta,datetime
import re

playlists={
    'crash course statics':'https://www.youtube.com/playlist?list=PL8dPuuaLjXtNM_Y-bUAhblSAdWRnmBUcr',
    'crash course computer science':'https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo',
    'khan academy statistics': 'https://www.youtube.com/playlist?list=PL1328115D3D8A2566',
    'NPTEL German 1': 'https://www.youtube.com/playlist?list=PLOSWwFV98rfIAPwtGN6rfb_LzPTo6LGaF',
    'NPTEL Deep learning': 'https://www.youtube.com/playlist?list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT'
}

time=re.compile('/d:/d')
html=urlopen(playlists['NPTEL Deep learning'])
bs=BeautifulSoup(html,'html.parser')

delta=[]
for link in bs.find_all('div' , {'class':'timestamp'}):
    try:
        t=datetime.strptime(link.getText(),"%M:%S")
        delta.append(timedelta(minutes=t.minute, seconds=t.second))
    except Exception as e:
        #print(e)
        #print(link.getText())
        t=datetime.strptime(link.getText(),"%H:%M:%S")
        delta.append(timedelta(hours = t.hour, minutes=t.minute, seconds=t.second))
        #print(len(delta))
    #print(link, link.getText())
    #total = total + timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds()


secon=0
for sec in delta:
    secon+=sec.total_seconds()

print("Seconds:"+str(secon))
print("Minutes:"+str(secon/60))
print("Hours:"+str(secon/3600))