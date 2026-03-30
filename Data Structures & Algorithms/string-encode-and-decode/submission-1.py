class Solution:

    def encode(self, strs: List[str]) -> str:
        # so we want to convert a list of strings to a string
        s = list()
        for st in strs:
            s.append(str(len(st)))
            s.append("#")
            s.append(st)
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        strs = list()
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            string = s[i:j]
            strs.append(string)
            i = j
        return strs
