class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oddCountFound = False
        allZeros = True

        for bit in range(32):
            oneCount = 0

            for num in nums:
                if ((num >> bit) & 1) == 1:
                    oneCount += 1

                if bit == 0:
                    if num != 0:
                        allZeros = False

            if oneCount % 2 != 0:
                oddCountFound = True
                break

        if allZeros:
            return 0

        n = len(nums)
        return n if oddCountFound else n - 1