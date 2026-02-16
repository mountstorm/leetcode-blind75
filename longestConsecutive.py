class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hasNext = set(nums)
        count = 0

        for i in hasNext:
            if i - 1 not in hasNext:
                current = i
                streak = 1
                while current + 1 in hasNext:
                    current += 1
                    streak += 1
                count = max(streak, count)
                
        return count
