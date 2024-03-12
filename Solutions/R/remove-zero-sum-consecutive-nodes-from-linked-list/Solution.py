# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class Solution:
    def removeZeroSumSublists(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        last = {}

        def work(head, pref):
            last[pref] = head
            if head:
                head. next = work(head. next, pref + head. val)
            return last[pref]
        return work(head, 0)
