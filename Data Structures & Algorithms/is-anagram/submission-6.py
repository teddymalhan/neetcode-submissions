class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True

        if len(s) != len(t):
            return False
        
        def charFreq(s: str) -> List[int]:
            charF = [0]*26
            for c in s:
                charF[ord(c)-ord('a')] += 1
            return charF
        
        if charFreq(s) != charFreq(t):
            return False
        
        return True