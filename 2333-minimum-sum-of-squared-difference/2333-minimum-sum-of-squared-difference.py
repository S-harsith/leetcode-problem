class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        n = len(nums1)
        k = k1 + k2
        diff = [0] * n
        largest = 0
        sum_diff = 0
        for i in range(n):
            diff[i] = abs(nums1[i] - nums2[i])
            largest = max(largest, diff[i])
            sum_diff += diff[i]
        if sum_diff <= k:
            return 0
        freq = [0] * (largest + 1)
        for value in diff:
            freq[value] += 1
        for i in range(largest, 0, -1):
            if k == 0:
                break
            if freq[i] == 0:
                continue
            if k >= freq[i]:
                k -= freq[i]
                freq[i - 1] += freq[i]
                freq[i] = 0
            else:
                freq[i - 1] += k
                freq[i] -= k
                k = 0
        result = 0
        for i in range(largest + 1):
            result += freq[i] * i * i
        return result