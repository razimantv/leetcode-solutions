# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                if (
                    cur.next.next.next
                    and cur.next.val == cur.next.next.next.val
                ):
                    cur.next = cur.next.next
                else:
                    cur.next = cur.next.next.next
            else:
                cur = cur.next
        return dummy.next
