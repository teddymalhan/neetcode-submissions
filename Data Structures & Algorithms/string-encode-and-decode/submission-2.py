class Solution:

    def encode(self, strs: List[str]) -> str:
        # gonna keep a list and convert it into a string later
        someList = list()
        for s in strs:
            someList.append(str(len(s)))
            someList.append("#")
            someList.append(s)
        return "".join(someList)

    # stored in <num><chars><num><chars>
    def decode(self, s: str) -> List[str]:
        strs = list()
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i, j = j+1, j+1
            for _ in range(length):
                j += 1
            strs.append(s[i:j])
            i = j
        
        return strs
