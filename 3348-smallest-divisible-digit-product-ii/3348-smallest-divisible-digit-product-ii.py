class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        need = []
        for p in (2, 3, 5, 7):
            e = 0
            while t % p == 0:
                t //= p
                e += 1
            need.append(e)
        if t != 1:
            return "-1"
        NEED = tuple(need)
        n = len(num)

        DIG = {1:(0,0,0,0), 2:(1,0,0,0), 3:(0,1,0,0), 4:(2,0,0,0),
               5:(0,0,1,0), 6:(1,1,0,0), 7:(0,0,0,1), 8:(3,0,0,0), 9:(0,2,0,0)}

        def sub(s, d):
            e = DIG[d]
            return (max(0,s[0]-e[0]), max(0,s[1]-e[1]),
                    max(0,s[2]-e[2]), max(0,s[3]-e[3]))

        def cost(s):
            """min digits needed to cover state s"""
            a, b, c, d = s
            no6 = -(-a // 3) + -(-b // 2)
            one6 = 1 + -(-max(0, a-1) // 3) + -(-max(0, b-1) // 2)
            return min(no6, one6) + c + d

        def build(s, k):
            """smallest k-digit zero-free string covering s (assumes feasible)"""
            out = []
            for i in range(k):
                rem = k - i - 1
                for d in range(1, 10):
                    nxt = sub(s, d)
                    if cost(nxt) <= rem:
                        out.append(str(d)); s = nxt; break
            return "".join(out)

        # prefix states, valid up to (and including) the first '0'
        pref = [NEED] * (n + 1)
        last = n - 1
        s = NEED
        for i, ch in enumerate(num):
            if ch == '0':
                last = i
                break
            s = sub(s, int(ch))
            pref[i + 1] = s

        # Case 0: num itself qualifies
        if '0' not in num and pref[n] == (0, 0, 0, 0):
            return num

        # Case 1: keep num[:i], raise digit i, fill the rest
        for i in range(last, -1, -1):
            base = pref[i]
            rem = n - i - 1
            for d in range(int(num[i]) + 1, 10):
                nxt = sub(base, d)
                if cost(nxt) <= rem:
                    return num[:i] + str(d) + build(nxt, rem)

        # Case 2: must grow — first digit is NOT forced to 1
        m = max(n + 1, cost(NEED))
        return build(NEED, m)