class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # clearly index of num_to_str corresponds to the string with the values needed to be searched through
        num_to_str: List[str] = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        max_length: int = len(digits)
        res = []
        # i represents the value of the digits being considered till now
        # string represents the string till now
        def dfs(i: int, string: str):
            nonlocal res
            # once we hit max we return the string till that point
            if i >= max_length:
                res.append(string)
                return
            # now according to each of the i values we can search through the state diagram and find the corresponding values to build it
            # num_to_str gets the string associated with that i value (digits[i] gets the corresponding string)
            # with this we get a list like ['a', 'b', 'c'] to search through
            # at this point we have a string which has been built say 'a'
            for elem in list(num_to_str[int(digits[i])]):
                # what this does is build the string incrementally
                dfs(i+1, string + str(elem))
        
        dfs(0, '')
        return res
        