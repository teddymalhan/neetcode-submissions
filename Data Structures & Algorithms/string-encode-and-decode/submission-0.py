class Solution:
    def encode(self, strs: List[str]) -> str:
        string = []
        for s in strs:
            string.append(str(len(s)))
            string.append("#")
            string.append(s)
        return "".join(string)
            
    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j += length + 1
            word = s[i:j]
            strs.append(word)
            i = j

        return strs
        
            
