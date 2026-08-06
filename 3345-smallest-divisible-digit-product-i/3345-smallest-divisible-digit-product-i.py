class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        num = n

        while True:
            temp = num
            product = 1

            while temp > 0:
                product *= temp % 10
                temp //= 10

            if product % t == 0:
                return num

            num += 1