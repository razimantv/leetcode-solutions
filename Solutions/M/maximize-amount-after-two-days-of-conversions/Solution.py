# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions

class Solution:
    def maxAmount(
        self, initial: str, pairs1: List[List[str]], rates1: List[float],
        pairs2: List[List[str]], rates2: List[float]
    ) -> float:
        def graph(pairs, rates):
            adj = defaultdict(list)
            for (u, v), w in zip(pairs, rates):
                adj[u]. append((v, w))
                adj[v].append((u, 1 / w))
            return adj

        def work(adj, u, ret):
            for v, w in adj[u]:
                if v not in ret:
                    ret[v] = ret[u] * w
                    work(adj, v, ret)

        adj1, adj2 = graph(pairs1, rates1), graph(pairs2, rates2)
        conv1, conv2 = {initial: 1}, {initial: 1}
        work(adj1, initial, conv1)
        work(adj2, initial, conv2)

        ret = 1
        for k, v in conv1.items():
            if k in conv2:
                ret = max(ret, v / conv2[k])
        return ret
