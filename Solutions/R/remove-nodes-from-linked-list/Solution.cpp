// https://leetcode.com/problems/remove-nodes-from-linked-list/

class Solution {
 public:
  pair<int, ListNode*> work(ListNode* node) {
    if (!node) return {0, node};
    auto [val, next] = work(node->next);
    node->next = next;
    if (val > node->val)
      return {val, next};
    else
      return {node->val, node};
  }
  ListNode* removeNodes(ListNode* head) { return work(head).second; }
};
