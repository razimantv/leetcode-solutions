# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        s = [ord(c) - ord('a') for c in s]
        elems = set(s)
        if k == 26 or len(elems) < k:
            return 1
        elif len(elems) < 26:
            tries = [i for i in range(26) if i not in elems][:1]
        else:
            tries = list(range(26))

        n = len(s)
        nextpos = [n] * 26
        nextposar = [[] for i in range(n)] + [nextpos.copy()]
        nextpiece, pieces = [n] * (n + 1), [0] * (n + 1)

        # For each position, find where the piece starting here ends
        #   = k+1th largest 'next' parameter
        for i in range(n-1, -1, -1):
            nextpos[s[i]] = i
            nextpiece[i] = sorted(nextpos)[k]
            pieces[i] = pieces[nextpiece[i]] + 1
            nextposar[i] = nextpos.copy()
        ret = pieces[0]

        def nextpiecemod(start, i, x):
            # Where does the next piece of start begin if we change s[i] to x
            snext = nextposar[start].copy()
            if snext[s[i]] == i:
                snext[s[i]] = nextposar[i + 1][s[i]]
            if snext[x] > i:
                snext[x] = i
            return sorted(snext)[k]

        # Use this to find number of pieces starting from here
        # For each position, for each possible change of character, find where that piece ends
        start, delta = 0, 0
        for i in range(n):
            for x in tries:
                if x == s[i]:
                    continue
                newnextpiece = nextpiecemod(start, i, x)
                if (newnextpiece, newnextpiece) > (nextpiece[start], i):
                    continue
                if newnextpiece > i:
                    ret = max(ret, delta + pieces[newnextpiece] + 1)
                else:
                    newsecondpiece = nextpiecemod(i, i, x)
                    ret = max(ret, delta + pieces[newsecondpiece] + 2)
            if i == nextpiece[start]:
                start, delta = i, pieces[0] - pieces[i]
        return ret
