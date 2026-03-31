class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[None]*len(s) for _ in range(len(s))]
        def isPalindrome(i: int, j: int) -> bool:
            if dp[i][j] != None:
                return dp[i][j]
    
            t = s[i:j+1]
            l, r = 0, len(t) - 1
            while l <= r:
                if t[l] == t[r]:
                    l += 1
                    r -= 1
                else:
                    dp[i][j] = False
                    return dp[i][j]
            dp[i][j] = True
            return dp[i][j]
        
        if len(s) == 1:
            return s
    
        maxLen, stringToSave = 0, ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        stringToSave = s[i:j+1]
        
        numberOfTrues = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] == True:
                    numberOfTrues += 1

        return numberOfTrues