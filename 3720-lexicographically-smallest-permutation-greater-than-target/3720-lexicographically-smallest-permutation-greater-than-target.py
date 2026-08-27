class Solution:
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        ans = []
        n = len(s)

        for i in range(n):
            t = ord(target[i]) - 97

            if cnt[t] == 0:
                for c in range(t + 1, 26):
                    if cnt[c] > 0:
                        res = ans + [chr(c + 97)]
                        cnt[c] -= 1

                        for j in range(26):
                            res += [chr(j + 97)] * cnt[j]

                        return ''.join(res)
                break

            ans.append(target[i])
            cnt[t] -= 1

        for i in range(len(ans) - 1, -1, -1):
            x = ord(ans[i]) - 97
            cnt[x] += 1

            t = ord(target[i]) - 97

            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    res = ans[:i] + [chr(c + 97)]
                    cnt[c] -= 1

                    for j in range(26):
                        res += [chr(j + 97)] * cnt[j]

                    return ''.join(res)

        return ""