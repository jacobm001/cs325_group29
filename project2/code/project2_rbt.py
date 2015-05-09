def addTwo(first,second):
    return [[x+y for x,y in zip(first[0],second[0])],
                    first[1]+second[1]]

def changeslow(array,K):
    if array.__contains__(K):
        out=[0]*len(array)
        out[array.index(K)]=1
        return [out,1]
    else:
        minimum=None
        for i in array:
            if not i<K:break
            result1=changeslow(array,i)
            result2=changeslow(array,K-i)
            result=addTwo(result1,result2)
            if minimum==None or result[1]<minimum[1]:
                minimum=result
        return minimum

def changegreedy(array,K):
    if array.__contains__(K):
        out=[0]*len(array)
        out[array.index(K)]=1
        return [out,1]
    else:
        biggest=array[-1]
        for i in range(len(array)-2,-1,-1):
            if biggest<=K:
                break
            else:
                biggest=array[i]
        howmany=int(K/biggest)
        result1=[[],0]
        if K!=howmany*biggest:
            result1=changegreedy(array,K-(howmany*biggest))
        result2=[0]*len(array)
        result2[array.index(biggest)]=howmany
        result2=[result2,howmany]
        return addTwo(result1,result2)

def changedp(array,K):
    table={}
    rows=[(i,j) for i,j in enumerate(array)]
    cols=[(i,j) for i,j in enumerate(range(K+1))]
    
    for row in rows:
        r,rv=row
        table[r]=[]
        for col in cols:
            c,cv=col
            if r==0 and c==0:
                frm=(0,0)
                table[r]+=[(0,frm)] 
            elif r==0:#top row
                backval=table[r][c-rv][0]+1
                frm=(r,c-rv)
                table[r]+=[(backval,frm)]   
            elif cv<rv:#beginning of a row
                rowabove=r-1
                cellaboveval=table[rowabove][c][0]
                frm=(r-1,c)
                table[r]+=[(cellaboveval,frm)]
            else:#last part of a row
                rowabove=r-1
                cellaboveval=table[rowabove][c][0]
                backval=table[r][c-rv][0]+1
                if cellaboveval<backval:
                    frm=(r-1,c)
                    table[r]+=[(cellaboveval,frm)]
                else:
                    frm=(r,c-rv)
                    table[r]+=[(backval,frm)]                  
    
    out=[0]*len(array)
    r=len(table)-1
    c=len(table[r])-1
    mincoins=table[r][c][0]
    current=(r,c)
    pcol=current[1]
    while True:
        r=current[0]
        c=current[1]
        rv=rows[r][1]
        
        current=table[r][c][1]#next
        ccol=current[1]
        if ccol!=pcol:
            out[array.index(rv)]+=1
        pcol=ccol

        if c==0:break
    return [out,mincoins]
    
if __name__=='__main__': 
    # test 1
    # all should return [1,1,1,1]
    A = 15
    V = [1,2,4,8]
    print 'Test 1'
    print '  greedy: ', changegreedy(V,A)
    print '  slow:   ', changeslow(V,A)
    print '  dp:     ', changedp(V,A)
    
    # test 2
    # greedy should return [2,1,0,2]
    # slow and dp should return [0,1,2,1]
    A = 29
    V = [1,3,7,12]
    print 'Test 2'
    print '  greedy: ', changegreedy(V,A)
    print '  slow:   ', changeslow(V,A)
    print '  dp:     ', changedp(V,A)

    # test 3
    # all should return [0,0,1,2]
    A = 31
    V = [1,3,7,12]
    print 'Test 3'
    print '  greedy: ', changegreedy(V,A)
    print '  slow:   ', changeslow(V,A)
    print '  dp:     ', changedp(V,A)
