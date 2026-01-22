class Solution:
    def topKFrequent(self, nums : List[int], k : int) -> List[int]:
        # HashMap to record numbers with frequency
        freqMap = {}

        for num in nums:
            if num in freqMap: 
                freqMap[num] += 1
            else: 
                freqMap[num] = 1

        sorted_fMap = sorted(freqMap, key = freqMap.get, reverse = True)

        return sorted_fMap[:k]
