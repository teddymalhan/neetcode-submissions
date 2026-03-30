class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if the set of these two values length == length of list and length of this list > maxLen:
        # add this as maxSubstring and update maxLen

        # loop:
        # increment the r pointer
        # increment l in a while loop of sorts until it reaches this red condition

        charSet, l, maxLength = set(),0, 0

        for r in range(len(s)):
            # if we have unique characters
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength