class Solution:
    def getDirections(
        self, root: Optional[TreeNode], start: int, end: int
    ) -> str:
        def rootpath(u, x, path):
            if u.val == x:
                return True
            for v, label in zip([u.left, u.right], 'LR'):
                path. append(label)
                if v and rootpath(v, x, path):
                    return True
                path.pop()
            return False

        p1, p2 = [], []
        rootpath(root, start, p1)
        rootpath(root, end, p2)

        l, n = 0, min(len(p1), len(p2))
        while l < n and p1[l] == p2[l]:
            l += 1

        return 'U' * len(p1[l:]) + ''. join(p2[l:])
