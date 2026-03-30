class Solution:
    def numDecodings(self, s: str) -> int:
        # to convert num to string 
        # do chr(<number> + ord('a') - 1) (-1 since we start from 1 not 0 in this mapping)
        if len(s) == 2 and s[0] == "0":
            return 0
        
        # another rule is
        # if s[i] and s[i+1] == "0" then shortcircuit the choice and start from i+2 and treat i and i+1 as a single character
        # mapping between i index and numberOfWays
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
