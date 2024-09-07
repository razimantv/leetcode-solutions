// https://leetcode.com/problems/add-two-numbers

class Solution {
 public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2, int carry = 0) {
    if (l1 == nullptr and l2 == nullptr and carry == 0) return nullptr;
    if (l1 != nullptr) {
      carry += l1->val;
      l1 = l1->next;
    }
    if (l2 != nullptr) {
      carry += l2->val;
      l2 = l2->next;
    }

    ListNode* ret = new ListNode(carry % 10);
    ret->next = addTwoNumbers(l1, l2, carry / 10);
    return ret;
  }
};
