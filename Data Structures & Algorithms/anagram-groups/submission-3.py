class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagramFreq(s: str)-> List[int]:
            anagramFreq = [0]*26;
            for s in str:
                anagramFreq[ord(s) - ord('a')] += 1
            return anagramFreq
        
        result = defaultdict(list)
        for s in strs:
            result[tuple(anagramFreq(s))].append(s)
        
        return result.values()