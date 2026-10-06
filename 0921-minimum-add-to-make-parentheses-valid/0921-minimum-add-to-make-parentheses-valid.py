class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open = 0
        count = 0
        for ch in s:
            if ch == '(':
                open += 1
            elif open == 0:
                count += 1
            else:
                open -= 1
        return open + count