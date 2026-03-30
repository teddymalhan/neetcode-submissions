class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def charFreq(s: str) -> Tuple[int]:
            charF = [0]*26
            for c in s:
                charF[ord(c) - ord('a')] += 1
            # used tuple now since it's immutable and hence hashable
            return tuple(charF)
        
        charFrequencyDict = defaultdict(list)
        for s in strs:
            charFrequencyDict[charFreq(s)].append(s)
        
        return [x for x in charFrequencyDict.values()]