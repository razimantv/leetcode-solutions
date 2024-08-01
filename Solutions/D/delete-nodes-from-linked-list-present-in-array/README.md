# Delete nodes from linked list present in array

[Problem link](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = set(nums)

        def work(head):
            if not head:
                return head
            elif head.val in nums:
                return work(head.next)
            head.next = work(head.next)
            return head
        return work(head)
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Linked list](/Collections/linked-list.md#linked-list) > [Recursion](/Collections/linked-list.md#recursion)
