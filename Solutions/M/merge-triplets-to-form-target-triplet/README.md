# Merge triplets to form target triplet

[Problem link](https://leetcode.com/problems/merge-triplets-to-form-target-triplet)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet

class Solution {
 public:
  bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
    vector<int> a(3);
    for (int i = 0, N = triplets.size(); i < N; ++i) {
      for (int j = 0; j < 3; ++j)
        if (triplets[i][j] > target[j]) goto BPP;
      for (int j = 0; j < 3; ++j) a[j] = max(a[j], triplets[i][j]);
    BPP:;
    }
    return a == target;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
