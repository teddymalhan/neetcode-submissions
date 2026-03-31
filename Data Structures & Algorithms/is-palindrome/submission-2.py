class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = filter(lambda x: isalpha(x) or isdigit(x), s)
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True