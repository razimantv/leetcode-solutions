// https://leetcode.com/problems/merge-k-sorted-lists

class Solution {
 public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    ListNode head, *tail = &head;
    auto cmp = [](const ListNode* n1, const ListNode* n2) {
      return n1->val < n2->val;
    };
    multiset<ListNode*, decltype(cmp)> m(cmp);
    for (auto n : lists)
      if (n) m.insert(n);
    while (!m.empty()) {
      auto n = *m.begin();
      m.erase(m.begin());
      tail->next = n;
      tail = n;
      if (n->next) m.insert(n->next);
    }
    tail->next = nullptr;
    return head.next;
  }
};
