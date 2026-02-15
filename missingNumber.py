class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # expected sum
        expected = 0
        total = 0
        # n is range so with the range, we can find the sum
        expected = len(nums) * (len(nums) + 1) / 2
        total = sum(nums)
        # if [0,1,3] total is 4, expected is 3 * 4 / 2 = 6. So, 6 - 4 = 2
        missing_number = expected - total

        return int(missing_number)
