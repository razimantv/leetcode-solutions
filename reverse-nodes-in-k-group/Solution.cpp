// https://leetcode.com/problems/reverse-nodes-in-k-group

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
 public:
  ListNode* reverseKGroup(ListNode* head, int k) {
    if (k == 1) return head;

    ListNode dummy(0, head);
    ListNode *cur = &dummy, temp;
    while (1) {
      auto temp = cur->next;
      for (int i = 0; i < k; ++i, temp = temp->next)
        if (!temp) return dummy.next;

      ListNode *f = cur->next, *l = f;
      for (int i = 1; i < k; ++i) {
        temp = l->next->next;
        l->next->next = f;
        f = l->next;
        l->next = temp;
      }

      cur->next = f;
      cur = l;
    }
    return dummy.next;
  }
};
