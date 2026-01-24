class Solution(object):
    # Two ways exist to solve the problem, I have both in this file:
        # 1. sorting & finding from the sorted list if contains duplicate
        # 2. using hashSet, where you iterate thru the list.
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort the list
        nums.sort()
        n = len(nums)

        for i in nums:
            if (nums[i] == nums[i + 1]):
                return True
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        #  hashSet for seen numbers
        seen = set()
        # iterate with num in nums
        for num in nums:
            # if number is in seen (hashSet), duplicate found
            if num in seen:
                return True
            # otherwise, add to the set for future lookups
            seen.add(num)
        return False

        
        
        
