'''
lower_bound of x is first element>=x
arr[] = [1,3,4,6,7,8,8,10,12,13]
x = 5
low = 0
high = len(arr)-1

'''
def lower_bound(arr,n,x): #l: list , n: len of list, x: search element
    ans = n
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]>=x):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
l = [1,2,3,3,5,6,8,9]    
print(l[lower_bound(l,len(l),4)])