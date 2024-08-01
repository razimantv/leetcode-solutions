# Validate binary tree nodes

[Problem link](https://leetcode.com/problems/validate-binary-tree-nodes/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        degree = [0] * n
        for x in left+right:
            if x == -1:
                continue
            if degree[x]:
                return False
            degree[x] = 1
        roots = [i for i in range(n) if not degree[i]]
        if len(roots) != 1:
            return False
        seen = [False] * n

        def dfs(u):
            seen[u] = True
            for v in [left[u], right[u]]:
                if v != -1:
                    dfs(v)
        dfs(roots[0])

        return len([u for u in range(n) if not seen[u]]) == 0
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Degree counting](/Collections/graph-theory.md#degree-counting)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
