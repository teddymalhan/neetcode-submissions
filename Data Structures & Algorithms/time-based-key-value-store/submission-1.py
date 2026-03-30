class TimeMap:
    # O(m*n) space: m total number of keys, n total number of values
    def __init__(self):
        # we're not given m and k at the start ofc
        self.keyStore = defaultdict(list)

    # O(1) time complexity
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append([value, timestamp])

    # O(logn) time complexity
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        
        # this is the list we have to search for
        listToSearch = self.keyStore[key]
        l, r = 0, len(listToSearch) - 1
        while l <= r:
            mid = (l+r)//2
            if listToSearch[mid][1] == timestamp:
                return listToSearch[mid][0]
            if listToSearch[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        if r < 0: return ""
        return listToSearch[r][0]