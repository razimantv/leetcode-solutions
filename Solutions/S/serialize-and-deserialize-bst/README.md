# Serialize and deserialize bst

[Problem link](https://leetcode.com/problems/serialize-and-deserialize-bst)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/serialize-and-deserialize-bst

class Codec {
 public:
  // Encodes a tree to a single string.
  string serialize(TreeNode* root, bool start = true) {
    if (root == NULL) return "[]";
    string ret = start ? "[" : "";
    ret += to_string(root->val);
    if (root->left != NULL) ret += "," + serialize(root->left, false);
    if (root->right != NULL) ret += "," + serialize(root->right, false);
    if (start) ret += "]";
    return ret;
  }

  TreeNode* gentree(const vector<int>& order, int start, int end) {
    TreeNode* ret = new TreeNode(order[start]);
    int mid = start + 1;
    while (mid < end and order[mid] < order[start]) ++mid;
    if (mid != start + 1) ret->left = gentree(order, start + 1, mid);
    if (mid != end) ret->right = gentree(order, mid, end);
    return ret;
  }

  // Decodes your encoded data to tree.
  TreeNode* deserialize(string data) {
    if (data == "[]") return NULL;
    vector<int> order;
    for (int i = 1, N = data.size(), cur = 0; i < N; ++i) {
      if (data[i] == ',' or data[i] == ']') {
        order.push_back(cur);
        cur = 0;
      } else {
        cur = cur * 10 + (data[i] - '0');
      }
    }

    return gentree(order, 0, order.size());
  }
};
```