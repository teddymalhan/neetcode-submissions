class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq map
        # num -> freq
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1

        # reverse map
        # freq to nums
        reverseFreqList = [[] for i in range(len(nums) + 1)]
        for key, val in freqMap.items():
            reverseFreqList[val].append(key)
        
        # reverse walk
        # take k elements and keep on subtracting
        # return then
        outputList = []
        elementsTaken = 0
        for i in range(len(reverseFreqList) - 1, -1, -1):
            if elementsTaken == k:
                break
            if len(reverseFreqList[i]) > 0:
                outputList.append(reverseFreqList[i].pop())
                elementsTaken += 1
        return outputList
