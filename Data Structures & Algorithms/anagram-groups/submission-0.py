class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagramFreq(s: str) -> list:
            # 0s from a to z
            countS = [0]*26
            for i in range(len(s)):
                # you set the corresponding, s[i] meaning
                countS[ord(s[i]) - ord('a')] += 1
            return countS

        freq = defaultdict(list)
        for s in strs:
            freq[tuple(anagramFreq(s))].append(s)
            
        return list(freq.values())