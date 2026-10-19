class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        count = 0
        start = 0

        for num in nums:
            if num == target:
                count += 1
            if num < target:
                start += 1

        while count != 0:
            res.append(start)
            start += 1
            count -= 1

        return res