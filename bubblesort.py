def bubblesort(data):
    print('原始資料為:')
    listprint(data)
    for i in range(len(data)-1,-1,-1):
        for j in range(i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]

    print('排序結果為:')
    listprint(data)

def listprint(data):
    for j in range(len(data)):
        print('%3d'%data[j],end=' ')
    print()

data=[16,25,39,27,12,8,45,63,1]
bubblesort(data)
