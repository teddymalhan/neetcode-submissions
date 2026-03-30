class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = list(filter(lambda c: c.isalpha() or c.isdigit(), map(lambda c: c.lower(), s)))
        l, r = 0, len(filtered) - 1
        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l += 1
            r -= 1
        
        return True

