# https://leetcode.com/problems/merge-nodes-in-between-zeros

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        while head.next.val != 0:
            head.val += head.next.val
            head.next = head.next.next
        head.next = self.mergeNodes(head.next)
        return head
