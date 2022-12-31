# leetcode 153
'''
nums = [3,4,5,1,2]
'''
def minimum_rotated_array(arr):
    low = 0
    high = len(arr)-1
    while(low<high):
        mid = (low+high)//2
        if(arr[mid]<arr[high]):
            high = mid
        else:
            low = mid+1
    return arr[low]
print(minimum_rotated_array([3,4,5,0,1,2]))
