# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary to store 'seen' values
        seen = {}
        # using enum, we access the indexes of nums
        for i, num in enumerate(nums):
            # complement var is for finding the indexes of target faster
            complement = target - num
            if complement in seen:
                # return both indices, complement & current. 
                return [seen[complement], i]
                # not found! save for future lookups
            seen[num] = i
            # not able to find at all, then return empty index list
        return []
            
        
    
  
