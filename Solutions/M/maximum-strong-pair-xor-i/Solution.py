# https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Node:
    def __init__(self):
        self.child = [None, None]
        self.count = 0

    def add(self, n, pos):
        cur = self
        for pos in range(20, -1, -1):
            id = 1 if (n & (1 << pos)) else 0
            if cur.child[id] is None:
                cur.child[id] = Node()
            cur = cur.child[id]
            cur.count += 1

    def rem(self, n, pos):
        cur = self
        for pos in range(20, -1, -1):
            id = 1 if (n & (1 << pos)) else 0
            cur = cur.child[id]
            cur.count -= 1

    def get(self, n, pos):
        cur = self
        ret = 0
        for pos in range(20, -1, -1):
            id = 0 if (n & (1 << pos)) else 1
            if cur.child[id] is None or not cur.child[id].count:
                id = 1-id
            cur = cur.child[id]
            ret |= id << pos
        return ret


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        trie = Node()
        nums = sorted(nums)
        l, best = 0, 0
        for r, x in enumerate(nums):
            trie.add(x, 20)
            while nums[l] * 2 < x:
                trie.rem(nums[l], 20)
                l += 1
            best = max(best, x ^ trie.get(x, 20))
        return best
