import requests
import re

url='http://www.ncu.edu.tw/'
htmlfile=requests.get(url)
if htmlfile.status_code==requests.codes.ok:
    print('取得網頁資料成功')
    pattern=input('請輸入欲搜尋的字串:')
    if pattern in htmlfile.text:
        print('搜尋%s字串成功'%pattern)
    else:
        print('搜尋%s字串失敗'%pattern)
    name=re.findall(pattern,htmlfile.text)
    if name!=None:
        print('%s出現%d次'%(pattern,len(name)))
    else:
        print('%s出現0次'%pattern)
else:
    print('取得網頁資料失敗')

