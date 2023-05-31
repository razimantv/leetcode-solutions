# Triples with bitwise and equal to zero

[Problem link](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero

class Solution {
 public:
  int countTriplets(vector<int>& nums) {
    int two[1 << 16]{};
    for (int x : nums)
      for (int y : nums) ++two[x & y];
    int ret = 0;
    for (int x : nums)
      for (int y = 0; y < (1 << 16); ++y)
        if (!(x & y)) ret += two[y];
    return ret;
  }
};
```