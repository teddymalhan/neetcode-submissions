class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sLower = list(map(lambda c: c.lower(), s))
        filtered = list(filter(lambda x: x.isalpha() or x.isdigit(), sLower))
        l, r = 0, len(filtered) - 1        
        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l += 1
            r -= 1
        
        return True