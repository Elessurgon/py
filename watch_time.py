#for checking the Watch time of all videos in a youtube playlist

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import timedelta,datetime
import re

playlists={
    'crash course statics':'https://www.youtube.com/playlist?list=PL8dPuuaLjXtNM_Y-bUAhblSAdWRnmBUcr',
    'crash course computer science':'https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo',
    'khan academy statistics': 'https://www.youtube.com/playlist?list=PL1328115D3D8A2566'
    }

time=re.compile('/d:/d')
html=urlopen(playlists['khan academy statistics'])
bs=BeautifulSoup(html,'html.parser')

delta=[]

for link in bs.find_all('div' , {'class':'timestamp'}):
    t=datetime.strptime(link.getText(),"%M:%S")
    delta.append(timedelta(minutes=t.minute,seconds=t.second))

secon=0
for sec in delta:
    secon+=sec.total_seconds()

print("Seconds:"+str(secon))
print("Minutes:"+str(secon/60))
print("Hours:"+str(secon/3600))