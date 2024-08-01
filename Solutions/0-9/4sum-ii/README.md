# 4sum ii

[Problem link](https://leetcode.com/problems/4sum-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/4sum-ii

class Solution {
 public:
  int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C,
                   vector<int>& D) {
    unordered_map<int, int> ab;
    for (int a : A)
      for (int b : B) ab[a + b]++;
    int ret = 0;
    for (int c : C)
      for (int d : D) ret += ab[-(c + d)];
    return ret;
  }
};
```
## Tags

* [Meet in the middle](/Collections/meet-in-the-middle.md#meet-in-the-middle)
