#print all permutations
def recurPermute(ds,nums,ans,mpp):
    if(len(ds) == len(ds)):
        ans.append(ds)
        return
    for i in range(len(nums)):
        if(mpp[nums[i]]):
            continue
        else:
            ds.append(nums[i])
            mpp[nums[i]] = 1
            recurPermute(ds,nums,ans,mpp)
            mpp[nums[i]] = 0
            ds.pop()
def permute(nums):
    ans = []
    ds = []
    mpp = {}
    for i in nums:
        if i not in mpp:
            mpp[i] = 0
    recurPermute(ds,nums,ans,mpp)
    return ans
            
    
    