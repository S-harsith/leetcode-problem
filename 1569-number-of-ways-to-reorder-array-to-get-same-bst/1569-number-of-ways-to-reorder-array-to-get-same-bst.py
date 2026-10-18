class Solution(object):
    def numOfWays(self, nums):

        n = len(nums)
        born = [-1] * (n + 2)  
        for t, x in enumerate(nums):
            born[x] = t

        sizes, stack = 1, [0]  # MP
        for v in range(1, n + 2):
            while born[stack[-1]] > born[v]: 
                stack.pop()
                sizes *= v - stack[-1] - 1  
            stack.append(v)

        return (factorial(n) // sizes - 1) % (10**9 + 7)