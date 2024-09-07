# https://leetcode.com/problems/linked-list-in-binary-tree/

class Solution:
    def isSubPath(
        self, head: Optional[ListNode], root: Optional[TreeNode], start=1
    ) -> bool:
        if not head:
            return True
        elif not root:
            return False
        for child in [root.left, root.right]:
            if root.val == head.val and self.isSubPath(head.next, child, 0):
                return True
            if start and self.isSubPath(head, child, 1):
                return True
        return False
