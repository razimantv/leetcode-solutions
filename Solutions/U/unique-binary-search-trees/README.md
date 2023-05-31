# Unique binary search trees

[Problem link](https://leetcode.com/problems/unique-binary-search-trees)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/unique-binary-search-trees

class Solution {
 public:
  int numTrees(int n) {
    vector<int> cnt(n + 1, 0);
    cnt[0] = 1;

    for (int i = 1; i <= n; ++i)
      for (int j = 1; j <= i; ++j) cnt[i] += cnt[j - 1] * cnt[i - j];
    return cnt[n];
  }
};
```