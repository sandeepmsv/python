#subset sum II

def findsubsets(ind,nums,ds,ans):
    ans.append(ds.copy())
    for i in range(ind,len(nums)):
        if(i!= ind and nums[i]==nums[i-1]):
            continue
        ds.append(nums[i])
        findsubsets(i+1,nums,ds,ans)
        ds.pop()
def subsetswithdup(nums):
    ans = []
    ds = []
    nums.sort()
    findsubsets(0,nums,ds,ans)
    return ans 
nums = [1,2,2,2,3,3]
print(subsetswithdup(nums))            