#leetcode 154(hard)
def minimum_rotated_arrayii(arr):
    low = 0
    high = len(arr)-1
    while(low<high):
        mid = (low+high)//2
        if(arr[mid]<arr[high]):
            high = mid
        elif arr[mid]>arr[high]:
            low = mid+1
        else:
            high -=1
    return arr[high]
print(minimum_rotated_arrayii([3,3,4,7,1,1,2,2]))
print(minimum_rotated_arrayii([1,1,1,0,0,1]))
print(minimum_rotated_arrayii([1,0,0,1,1,1,1]))
print(minimum_rotated_arrayii([0,1,1,1,1,1,1,1,1,1]))



