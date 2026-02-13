class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointers technique
        left = 0
        right = len(height) - 1
        # final output to return
        max_area = 0

        while left < right: 
            # calculate current_area: W * H
            current_area = min(height[left], height[right) * (right - left)
            # move the pointers inwards accordingly
            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1

            # update the max_area
            max_area = max(current_area, max_area)

        return max_area

                

                
        
        
