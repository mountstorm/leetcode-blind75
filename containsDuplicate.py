class Solution(object):
    # Two ways exist to solve the problem, I have both in this file:
        # 1. sorting & finding from the sorted list if contains duplicate
        # 2. using hashSet, where you iterate thru the list.
    def containsDuplicate(self, nums):
        # sort the list
        nums.sort()
        n = len(nums)

        for i in range(1, n):
            if (nums[i] == nums[i - 1]):
                return True
        return False
