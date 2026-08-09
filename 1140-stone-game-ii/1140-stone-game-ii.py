class Solution(object):
    def stoneGameII(self, piles):
        dp = {}
        def score(alice, idx, M):
            if idx == len(piles):
                return 0
            if (alice, idx, M) in dp:
                return dp[(alice, idx, M)]
            if alice:
                res = 0
            else:
                res = float('inf')
            total = 0
            for x in range(1, 2 * M + 1):
                if idx + x > len(piles):
                    break
                total += piles[idx + x - 1]
                if alice:
                    res = max(res, total + score(not alice, idx + x, max(M, x)))
                else:
                    res = min(res, score(not alice, idx + x, max(M, x)))
            dp[(alice, idx, M)] = res
            return res
        return score(True, 0, 1)