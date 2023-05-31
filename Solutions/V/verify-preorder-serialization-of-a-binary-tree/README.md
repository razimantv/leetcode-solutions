# Verify preorder serialization of a binary tree

[Problem link](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree

class Solution {
 public:
  string gettoken(const string& s, int& i) {
    string ret;
    while (s[i] and s[i] != ',') ret += s[i++];
    if (s[i]) ++i;
    return ret;
  }
  bool isValidSerialization(string preorder) {
    if (preorder.size() == 1) return preorder[0] == '#';

    vector<int> v{0};
    for (int i = 0; preorder[i];) {
      string s = gettoken(preorder, i);
      if (v.empty()) return false;
      if (s[0] == '#') {
        while (1) {
          if (v.empty()) break;
          if (!v.back()) {
            ++v.back();
            break;
          }
          v.pop_back();
        }
      } else
        v.push_back(0);
    }
    return v.size() == 1 and v.back() == 1;
  }
};
```