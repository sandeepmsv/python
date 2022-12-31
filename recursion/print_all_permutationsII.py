#print_all_permutation 
def recurpermute(ind,nums,ans):
    if(ind==len(nums)):
        ans.append(nums)
        return
    for i in range(ind,len(nums)):
        nums[ind],nums[i] = nums[i],nums[ind]
        recurpermute(ind+1,nums,ans)
def permute(nums):
    ans = []
    recurpermute(0,nums,ans)
    return ans
 