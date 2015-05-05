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
        result1=changegreedy(array,K-(howmany*biggest))
        result2=[0]*len(array)
        result2[array.index(biggest)]=howmany
        result2=[result2,howmany]
        return addTwo(result1,result2)
    
    
    
print changeslow([1,2,4,8],15)
print changegreedy([1,2,4,8],15)
