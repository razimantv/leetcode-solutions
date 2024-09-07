// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/


class Solution {
 public:
  ListNode* deleteMiddle(ListNode* head) {
    if (!head or !head->next) return nullptr;
    ListNode *p1 = head, *p2 = p1->next;
    while (1) {
      if (!p2->next) {
        p1->next = p1->next->next;
        break;
      }
      p2 = p2->next;
      if (!p2->next) {
        p1->next = p1->next->next;
        break;
      }
      p2 = p2->next;
      p1 = p1->next;
    }
    return head;
  }
};
