# Distribute candies

[Problem link](https://leetcode.com/problems/distribute-candies)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/distribute-candies

class Solution {
 public:
  int distributeCandies(vector<int>& candyType) {
    int n = candyType.size(), types = 1;
    sort(candyType.begin(), candyType.end());

    for (int i = 1; i < n; ++i)
      if (candyType[i] != candyType[i - 1]) ++types;
    return min(types, n / 2);
  }
};
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Contiguous region](/README.md#Array_scanning-Contiguous_region)
* [Simple implementation](/README.md#Simple_implementation)
