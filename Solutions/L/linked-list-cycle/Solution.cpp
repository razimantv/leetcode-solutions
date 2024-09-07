// https://leetcode.com/problems/linked-list-cycle

class Solution {
 public:
  bool hasCycle(ListNode *head) {
    ListNode *fast = head;
    while (1) {
      if (fast == nullptr or fast->next == nullptr) return false;
      fast = fast->next->next;
      head = head->next;
      if (fast == head) return true;
    }
  }
};
