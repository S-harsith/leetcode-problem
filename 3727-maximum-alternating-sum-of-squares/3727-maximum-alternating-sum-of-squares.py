class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            nums[i] *= nums[i]
        nums.sort()
        ans = 0
        for i in range(n // 2):
            ans -= nums[i]
        for i in range(n // 2, n):
            ans += nums[i]
        return ans