# https://leetcode.com/problems/palindrome-rearrangement-queries/

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n, bad = len(s), []
        m = n // 2
        p1, p2 = [0] * 26, [0] * 26
        psum1, psum2 = [p1.copy()], [p2.copy()]
        for i in range(m):
            c, d = s[i], s[n-1-i]
            p1[ord(c) - ord('a')] += 1
            p2[ord(d) - ord('a')] += 1
            psum1.append(p1.copy())
            psum2.append(p2.copy())
            for x in range(26):
                if p1[x] != p2[x]:
                    bad.append(i)
                    break

        if not bad:
            return [True for q in queries]
        bd = set(bad)

        def simplify(a, b, c, d):
            r1, r2 = [a, b, 1], [n - 1 - d, n - 1 - c, 2]
            if r1[0] > r2[0] or (r1[0] == r2[0] and r1[1] < r2[1]):
                r1, r2 = r2, r1
            return [r1, r1] if r1[1] >= r2[1] else [r1, r2]

        def match(i, j):
            for x in range(26):
                if psum1[j+1][x] - psum1[i][x] != psum2[j+1][x] - psum2[i][x]:
                    return False
            return True

        def part(q1, q2, i1, j1, i2, j2):
            for x in range(26):
                if q1[j1 + 1][x] - q1[i1][x] < q2[j2 + 1][x] - q2[i2][x]:
                    return False
            return True

        for i, (a, b, c, d) in enumerate(queries):
            r1, r2 = simplify(a, b, c, d)
            if bad[0] < r1[0] or bad[-1] >= r2[1]:
                queries[i] = False
                continue
            if r1 == r2:
                queries[i] = True
            elif r1[1] < r2[0]:
                queries[i] = r1[1] not in bd and (
                    bad[-1] < r1[1] or bad[bisect_right(bad, r1[1])] >= r2[0]
                )
            else:
                q1, q2 = (psum1, psum2) if r1[-1] == 1 else (psum2, psum1)
                queries[i] = (
                    match(r1[0], r2[1]) and
                    part(q1, q2, r1[0], r1[1], r1[0], r2[0] - 1) and
                    part(q2, q1, r2[0], r2[1], r1[1] + 1, r2[1])
                )
        return queries
