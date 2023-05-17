// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class Solution {
 public:
  using ptr = ListNode*;
  pair<ptr, ptr> reverse(ptr head) {
    if (!head->next) return {head, head};
    auto [h, t] = reverse(head->next);
    t->next = head;
    head->next = nullptr;
    return {h, head};
  }
  int pairSum(ListNode* head) {
    auto mid = head, end = head->next;
    while (end->next) mid = mid->next, end = end->next->next;
    mid->next = reverse(mid->next).first;
    mid = mid->next;

    int ret{};
    while (mid) {
      ret = max(ret, head->val + mid->val);
      head = head->next;
      mid = mid->next;
    }
    return ret;
  }
};
