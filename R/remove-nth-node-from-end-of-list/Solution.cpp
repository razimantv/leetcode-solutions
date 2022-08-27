// https://leetcode.com/problems/remove-nth-node-from-end-of-list

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
  ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode *n1 = head, *n2 = n1;
    for (int i = 0; i < n; ++i) n2 = n2->next;
    if (n2 == nullptr) return n1->next;
    n2 = n2->next;
    while (n2 != nullptr) n1 = n1->next, n2 = n2->next;
    n1->next = n1->next->next;
    return head;
  }
};
