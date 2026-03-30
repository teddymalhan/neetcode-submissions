class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 2 and s[0] == "0":
            return 0
        
        n = len(s)
        numberOfWays = [0]*(n)

        def dfs(index: int):
            if index >= n:
                return 1
            
            if numberOfWays[index] != 0:
                return numberOfWays[index]

            # took one character
            ways = dfs(index+1) if s[index] != "0" else 0
            # can take two characters
            if index + 1 < n and 10 <= int(s[index:index+2]) <= 26:
                ways += dfs(index+2)
            return ways
    
        return dfs(0)
