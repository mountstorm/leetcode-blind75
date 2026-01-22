class Solution:
    def topKFrequent(self, nums : List[int], k : int) -> List[int]:
        # HashMap to record numbers with frequency
        freqMap = {}
        # use for loop to find frequency of the numbers (values) if not exist yet create one, unless increment by 1
        for num in nums:
            if num in freqMap: 
                freqMap[num] += 1
            else: 
                freqMap[num] = 1
        # sort the HashMap by descending order so that we easily access the top K elements
        sorted_fMap = sorted(freqMap, key = freqMap.get, reverse = True)
        # returns the elements from top 1 to kth index.
        return sorted_fMap[:k]
