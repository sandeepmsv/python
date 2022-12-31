# combination Sum
'''
ex: x = [2,3,6,7], target = 7
output: [[2,2,3],[7]]

'''
ans = []
ds = []
def combinationSum(arr,target):
   
    findCombination(0,target,arr,ans,ds)
    print(ans)

def findCombination(ind,target,arr,ans,ds):
    if(ind == len(arr)):
        if(target ==0):
            ans.append(ds.copy())
        return
    if arr[ind]<=target:
        ds.append(arr[ind])
        findCombination(ind,target-arr[ind],arr,ans,ds)
        
        ds.pop() 
    findCombination(ind+1,target,arr,ans,ds)


arr = [2,3,6,7]
target = 7
combinationSum(arr,7)