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

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
