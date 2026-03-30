class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(t: str) -> bool:
            l, r = 0, len(t) - 1
            while l <= r:
                if t[l] == t[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        if len(s) == 1:
            return s

        maxLen, stringToSave = 0, ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        stringToSave = s[i:j+1]
        
        return stringToSave