# Convert sorted list to binary search tree

[Problem link](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
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
```
## Tags

* [Tree](/Collections/tree.md#tree) > [Binary tree](/Collections/tree.md#binary-tree) > [Recursion](/Collections/tree.md#recursion)
* [Linked list](/Collections/linked-list.md#linked-list) > [Iteration](/Collections/linked-list.md#iteration)
