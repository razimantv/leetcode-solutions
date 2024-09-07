// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

class Solution {
 public:
  TreeNode* vecToBST(const vector<int>& vec, int l, int r) {
    if (r < l) return nullptr;
    int m = (l + r) >> 1;
    return new TreeNode(vec[m], vecToBST(vec, l, m - 1),
                        vecToBST(vec, m + 1, r));
  }

  TreeNode* sortedListToBST(ListNode* head) {
    vector<int> vec;
    while (head) vec.push_back(head->val), head = head->next;

    return vecToBST(vec, 0, vec.size() - 1);
  }
};
