
# prints all subsequence whose sum is sum
def printS(ind,ds,s,sum1,arr,n):
    if(ind==n):
        if(s==sum1):
            for i in ds:
                print(i,end = " ")
            print()
        return 
    ds.append(arr[ind])
    s += arr[ind]
    printS(ind+1,ds,s,sum1,arr,n)
    s -= arr[ind]
    ds.pop()
    # not pick
    printS(ind+1,ds,s,sum1,arr,n)
    
    




# print any subsequence whose sum is sum
def printS1(ind,ds,s,sum1,arr,n):
    if(ind==n):
        # condition Satisfied
        if(s==sum1):
            for i in ds:
                print(i,end = " ")
            print()
            return True
        else:
            return False
    ds.append(arr[ind])
    s += arr[ind]
    if(printS1(ind+1,ds,s,sum1,arr,n)):
        return True
    s -= arr[ind]
    ds.pop()
    # not pick
    if(printS1(ind+1,ds,s,sum1,arr,n)):
        return True
    return False



# count no subsequence whose sum is sum
def count_sub_sum(ind,s,sum1,arr,n):
    if(ind==n):
        # condition satisfied
        if(s==sum1):
            return 1
        # condition not satisfied
        else:
            return 0
    
    s += arr[ind]
    l = count_sub_sum(ind+1,s,sum1,arr,n)
    s -= arr[ind]

    # not pick
    r = count_sub_sum(ind+1,s,sum1,arr,n)
    return l+r








arr = [3,1,2]
ds = []
n = len(arr)
sum1 = 3


# printS(0,ds,0,sum1,arr,n)
# print(printS1(0,ds,0,sum1,arr,n))
print(count_sub_sum(0,0,sum1,arr,n))
