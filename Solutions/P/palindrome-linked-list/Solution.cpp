// https://leetcode.com/problems/palindrome-linked-list

class Solution {
 public:
  bool work(ListNode *head, int l, int r, ListNode *&cur) {
    if (l == r) {
      cur = head;
      return true;
    } else if (l + 1 == r) {
      cur = head->next;
      return head->val == cur->val;
    }

    return work(head->next, ++l, --r, cur) and
           (cur = cur->next)->val == head->val;
  }
  bool isPalindrome(ListNode *head) {
    ListNode *cur = head;
    int n = 0;
    while (cur != nullptr) ++n, cur = cur->next;
    return work(head, 0, n - 1, cur);
  }
};
