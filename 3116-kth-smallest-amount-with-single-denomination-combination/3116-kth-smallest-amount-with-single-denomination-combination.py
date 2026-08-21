class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        L = len(coins)
        from fractions import gcd
        def getLcm(x, y):
            if x == 0 or y == 0:
                return 0
            return abs(x * y) // gcd(x, y)
        def countBit(combination):
            count = 0
            while combination:
                combination &= combination - 1
                count += 1
            return count
        def can(target):
            count = 0
            for combination in range(1, 1 << L):
                lcm = 1
                for idx, coin in enumerate(coins):
                    if combination >> idx & 1:
                        lcm = getLcm(lcm, coin)
                        if lcm > target:
                            break
                else:
                    if countBit(combination) % 2 == 1:
                        count += target // lcm
                    else:
                        count -= target // lcm
            return count >= k
        left, right = 1, min(coins) * k
        while left + 1 < right:
            middle = (left + right) // 2
            if can(middle):
                right = middle
            else:
                left = middle + 1
        if can(left):
            return left
        else:
            return right