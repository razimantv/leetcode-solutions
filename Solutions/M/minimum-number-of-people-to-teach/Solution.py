# https://leetcode.com/problems/minimum-number-of-people-to-teach/

class Solution:
    def minimumTeachings(
        self, n: int, languages: list[list[int]], friendships: list[list[int]]
    ) -> int:
        knowers = [set() for _ in range(n)]
        for u, langlist in enumerate(languages):
            for l in langlist:
                knowers[l - 1].add(u)

        f = len(friendships)
        goodpair = [0] * f
        for lknowers in knowers:
            for i, (u, v) in enumerate(friendships):
                if u - 1 in lknowers and v - 1 in lknowers:
                    goodpair[i] = 1

        learners = set()
        for flag, (u, v) in zip(goodpair, friendships):
            if not flag:
                learners.add(u - 1)
                learners.add(v - 1)

        if not learners:
            return 0
        cnt = Counter()
        for u in learners:
            cnt.update(Counter(languages[u]))

        return len(learners) - cnt.most_common(1)[0][1]
