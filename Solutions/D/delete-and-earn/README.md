# Delete and earn

[Problem link](https://leetcode.com/problems/delete-and-earn)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/delete-and-earn

class Solution {
 public:
  int deleteAndEarn(vector<int>& nums) {
    unordered_map<int, int> m;
    for (int x : nums) m[x] += x;
    for (int x = 1; x <= 10000; ++x) m[x] = max(m[x] + m[x - 2], m[x - 1]);
    return m[10000];
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
