def combination(n,r):
    record_name=str(n)+' '+str(r)
    if record_name not in record:
        if r==1:
            record[record_name]=n
        elif r==n:
            record[record_name]=1
        else:
            record[record_name]=combination(n-1,r)+combination(n-1,r-1)
    return record[record_name]

record={}
print(combination(20,3))
        
