'''
Given x, find the number of occurences of x
x = 7
arr[] = [1,3,5,7,7,7,10]

'''
def occurences(arr,n,x):
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif(arr[mid]<x):
            low = mid+1
        else:
            high = mid-1
    return -1
l = [1,3,5,7,7,7,7,7,7,10,10,10,10,10]
k = 7
x = occurences(l,len(l),1)
i = x-1
j = x+1
cnt = 1
while(i>=0 and j<len(l)):
    if l[i]==k:
        cnt+=1
        i-=1
    elif l[j]==k:
        cnt+=1
        j+=1
    else:
        break
print(cnt)