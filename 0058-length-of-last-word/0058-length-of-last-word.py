class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        count = 0
        for i in s:
            if i != ' ':
                count += 1
            else:
                if count != 0:
                    l.append(count)
                    count = 0

        if count != 0:
            l.append(count)
        return l[-1] if l else 0