# https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

class Solution:
    def kthLargestPerfectSubtree(
        self, root: Optional[TreeNode], k: int
    ) -> int:
        allgood = []

        def dfs(root):
            if not root:
                return [True, 0]
            lf, lc = dfs(root.left)
            rf, rc = dfs(root. right)
            good, cnt = lf and rf and (lc == rc), lc + rc + 1
            if good:
                allgood.append(cnt)
            return [good, cnt]

        dfs(root)
        allgood.sort(reverse=True)
        return -1 if len(allgood) < k else allgood[k - 1]
