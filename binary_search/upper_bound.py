'''
upper_bound: first_element>x
arr[] = [1,3,4,6,6,7,9]
x = 6, ub = 5
x = 4, ub = 3
x = 5, ub = 3
x = 9, ub = 7
x = 10, ub = 7
'''
def upper_bound(arr,n,x):
    low = 0
    high = n-1
    ans = n
    while(low<=high):
        mid = (low+high)//2
        # if the mid is <=x, then we need to search on right
        if(arr[mid]<=x):
            low = mid+1
        # >x, then we need first, hence move left
        else:
            ans = mid
            high = mid-1
    return ans
l = [1,3,4,6,6,7,9,10,12,14]
print(l[upper_bound(l,len(l),13)])
            
        