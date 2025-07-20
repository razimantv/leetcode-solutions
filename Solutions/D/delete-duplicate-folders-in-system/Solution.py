# https://leetcode.com/problems/delete-duplicate-folders-in-system

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        class Node:
            def __init__(self):
                self.children = {}

        root = Node()

        def insert(path):
            node = root
            for part in path:
                if part not in node.children:
                    node.children[part] = Node()
                node = node.children[part]
        for path in paths:
            insert(path)

        cnt = Counter()

        def dfs(node):
            if not node.children:
                node.serial = ''
                return

            child_serials = []
            for child in sorted(node.children):
                cnode = node.children[child]
                dfs(cnode)
                child_serials.append(child + '(' + cnode.serial + ')')
            node.serial = ','.join(sorted(child_serials))
            cnt[node.serial] += 1
        dfs(root)

        ret = []

        def dfs2(node, path):
            for k, v in node.children.items():
                if cnt[v.serial] < 2:
                    path.append(k)
                    ret.append(copy.deepcopy(path))
                    dfs2(v, path)
                    path.pop()

        dfs2(root, [])

        return ret
