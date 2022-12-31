# subset sum-I
def f(ind,sum,arr,n,sumsubset):
    if(ind==n):
        sumsubset.append(sum)
        return
    # Pick the element
    f(ind+1,sum+arr[ind],arr,n,sumsubset)
    # Don't pick the element
    f(ind+1,sum,arr,n,sumsubset)
def subsetSums(arr,n):
    sumsubset = []
    f(0,0,arr,n,sumsubset)
    sumsubset.sort()
    return sumsubset
arr =  [3,1,2]
print(subsetSums(arr,len(arr)))   
    