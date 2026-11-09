class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        sCount = {}
        pCount = {}
        res = []
        l = 0

        for i in range(len(p)):
            if s[i] in sCount:
                sCount[s[i]] += 1
            else:
                sCount[s[i]] = 1

            if p[i] in pCount:
                pCount[p[i]] += 1
            else:
                pCount[p[i]] = 1

        if pCount == sCount:
            res = [0]

        for r in range(len(p), len(s)):
            if s[r] in sCount:
                sCount[s[r]] += 1
            else:
                sCount[s[r]] = 1

            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1

            if sCount == pCount:
                res.append(l)

        return res