class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return False
        
        def charFreq(s: str) -> List[int]:
            charFreqMap = [0]*26
            for c in s:
                charFreqMap[ord(c) - ord('a')] += 1
            return charFreqMap
        
        if charFreq(s) == charFreq(t):
            return True
        
        return False