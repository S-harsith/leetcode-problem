class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        bitCount = [0] * 31

        for num in nums:
            for b in range(31):
                if (num >> b) & 1:
                    bitCount[b] += 1

        ans = 0

        for i in range(k):
            val = 0

            for b in range(31):
                if bitCount[b] > i:
                    val |= (1 << b)

            ans = (ans + val * val) % MOD

        return ans