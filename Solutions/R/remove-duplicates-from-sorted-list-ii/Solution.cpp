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
