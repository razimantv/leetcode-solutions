# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

class Solution:
    def constructFromPrePost(
        self, preorder: list[int], postorder: list[int]
    ) -> Optional[TreeNode]:
        ret = TreeNode(preorder[0])
        if len(preorder) > 1:
            i = postorder.index(preorder[1])
            ret.left = self.constructFromPrePost(
                preorder[1:i + 2], postorder[:i + 1]
            )
            if i + 2 < len(preorder):
                ret.right = self.constructFromPrePost(
                    preorder[i + 2:], postorder[i + 1:-1]
                )
        return ret
