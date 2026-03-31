class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n) word formation (n length of longest string)
        def anagramFreq(s: word) -> List:
            freq = [0]*26
            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
            return freq
        
        # O(m) sweep
        
        freqDict = defaultdict(list)
        for i, elem in enumerate(strs):
            # lists are not indexable
            freqDict[tuple(anagramFreq(elem))] = elem
        
        return list(freqDict.values())
