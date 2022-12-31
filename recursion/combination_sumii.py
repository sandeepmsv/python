# combination Sum ii-(leetcode 40)
'''
arr[] = [1,1,1,2,2], target = 4
'''
ans = []
ds = []
def combinationSum(arr,target):
    arr.sort()
   
    findCombination2(0,target,arr,ans,ds)
    print(ans)

def findCombination2(ind,target,arr,ans,ds):
    if(target==0):
        ans.append(ds)
        return
    for i in range(ind,len(arr)):
        if(i>ind and arr[i] == arr[i-1]):
            continue
        if(arr[i]>target):
            break
             
        ds.append(arr[i])
        findCombination2(i+1,target-arr[i],arr,ans,ds)
        ds.pop()
        
        
            
   


arr = [2,3,6,7]
target = 7
combinationSum(arr,7)