class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        sorted_pairs = sorted([(nums[i], i) for i in range(n)])
        result = [0] * n
        group_start = 0
        for i in range(n):
            if i == n - 1 or sorted_pairs[i+1][0] - sorted_pairs[i][0] > limit:
                indices = [pair[1] for pair in sorted_pairs[group_start:i+1]]
                indices.sort()
                for j in range(len(indices)):
                    result[indices[j]] = sorted_pairs[group_start + j][0]
                group_start = i + 1
        return result