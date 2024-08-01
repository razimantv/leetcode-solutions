# Distribute candies to people

[Problem link](https://leetcode.com/problems/distribute-candies-to-people)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/distribute-candies-to-people

class Solution {
 public:
  vector<int> distributeCandies(int candies, int num_people) {
    vector<int> ret(num_people);
    for (int i = 0, n = 1; candies; ++i, ++n) {
      if (i == num_people) i = 0;
      ret[i] += min(n, candies);
      candies -= min(n, candies);
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
