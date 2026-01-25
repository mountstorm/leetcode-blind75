class Solution:
    def isPalindrome(self, s : str) -> bool:
        # new string with only nums and chars using .join and .isalnum()
        newS = "".join(c.lower() for c in s if c.isalnum())
        # right and left pointers
        left = 0
        right = len(newS) - 1
        # while left is not on same index as right pointer, loop continues
        while left <= right:
            # if char not matches on both ends, it is not Palindrome
            if newS[left] != newS[right]:
                return False
            # else, continue incrementing left, and decrementing right to check from two ends
            left += 1
            right -= 1
        # after comparing successfully, return True
        return True
    
