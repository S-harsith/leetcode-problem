class Solution:
    def validSequence(self, word1, word2):
        n, m = len(word1), len(word2)
        suffix = [m] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                suffix[i] = j
                j -= 1
        j = 0
        used_mismatch = False
        ans = []
        for i in range(n):
            if j >= m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not used_mismatch and suffix[i + 1] <= j + 1:
                used_mismatch = True
                ans.append(i)
                j += 1
        if j == m:
            return ans
        return []