# Remove zero sum consecutive nodes from linked list

[Problem link](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)

## Solutions


### Solution.py
```py
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
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Linked list](/Collections/linked-list.md#linked-list) > [Recursion](/Collections/linked-list.md#recursion)
