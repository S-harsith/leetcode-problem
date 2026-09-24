class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            if total == i:
                return i

        return -1