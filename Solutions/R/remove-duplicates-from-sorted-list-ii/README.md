# Remove duplicates from sorted list ii

[Problem link](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

class Solution {
 public:
  ListNode* deleteDuplicates(ListNode* head) {
    if (head == nullptr or head->next == nullptr) return head;
    if (head->val != head->next->val) {
      head->next = deleteDuplicates(head->next);
      return head;
    }
    int x = head->val;
    while (head != nullptr and head->val == x) head = head->next;
    return deleteDuplicates(head);
  }
};
```
### Solution.py
```py
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
```
## Tags

* [Linked list](/Collections/linked-list.md#linked-list) > [Recursion](/Collections/linked-list.md#recursion)
* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
