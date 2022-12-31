# palindromic partition
# leetcode-131
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def f(ind):
            if ind >= len(s):
                res.append(path.copy())
                return
            for j in range(ind, len(s)):
                if self.isPalindrome(s,ind,j):
                    path.append(s[ind:j+1])
                    f(j+1)
                    path.pop()
        f(0)
        return res
    def isPalindrome(self,s, l, r):
        while l <r:
            if s[l] != s[r]:
                return False
            l +=1
            r -=1
        return True
