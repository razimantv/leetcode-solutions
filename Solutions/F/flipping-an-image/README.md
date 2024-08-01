# Flipping an image

[Problem link](https://leetcode.com/problems/flipping-an-image)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/flipping-an-image

class Solution {
 public:
  vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
    for (auto& r : A) {
      reverse(r.begin(), r.end());
      for (int& x : r) x ^= 1;
    }
    return A;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
