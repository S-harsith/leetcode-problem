class Solution:
    def missingInteger(self, nums):
        # Intuition: sum sequential prefix, then linear scan for first missing value
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        candidate = total
        while True:
            if candidate not in nums:
                return candidate
            candidate += 1