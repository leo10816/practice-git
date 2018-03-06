def showdata(data):
    for i in range(len(data)):
        print('%3d'%data[i],end='')
    print()

def selectsort(data):
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            if data[i]>data[j]:
                data[i],data[j]=data[j],data[i]
    print()

data=[16,25,39,27,12,8,45,63]
print('原始資料為:')
showdata(data)
selectsort(data)
print('排序後資料:')
showdata(data)
