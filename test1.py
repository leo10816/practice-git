def filenamecount(urls):
    filenamedict={}
    for url in urls:
        split_url=url.split('/')
        filename=split_url[-1]
        if filename not in filenamedict:
            filenamedict[filename]=1
        else:
            filenamedict[filename]+=1
    sorted_filenamedict=sorted(filenamedict.items(),key=lambda value:value[1],reverse=True)
    return sorted_filenamedict

urls=[
'http://www.google.com/a.txt',
'http://www.google.com.tw/a.txt',
'http://www.google.com/download/c.jpg',
'http://www.google.co.jp/a.txt',
'http://www.google.com/b.txt',
'https://facebook.com/movie/b.txt',
'http://yahoo.com/123/000/c.jpg',
'http://gliacloud.com/haha.png']

result=filenamecount(urls)

for key,value in result[0:3]:
    print(key+' '+str(value))
        
