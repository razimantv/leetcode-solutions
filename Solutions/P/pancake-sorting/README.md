# Pancake sorting

[Problem link](https://leetcode.com/problems/pancake-sorting)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/pancake-sorting

class Solution {
 public:
  vector<int> pancakeSort(vector<int>& A) {
    vector<int> ret;
    for (int i = A.size(); i; --i) {
      int cur = find(A.begin(), A.end(), i) - A.begin() + 1;
      ret.push_back(cur);
      reverse(A.begin(), A.begin() + cur);
      ret.push_back(i);
      reverse(A.begin(), A.begin() + i);
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
