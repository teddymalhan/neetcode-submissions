class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagramFreq(s: str) -> List:
            countS = [0]*26
            for i in range(len(s)):
                countS[ord(s[i]) - ord('a')]+=1
            return countS
        
        seen = defaultdict(list)
        for s in strs:
            seen[tuple(anagramFreq(s))].append(s)
        
        return list(seen.values())