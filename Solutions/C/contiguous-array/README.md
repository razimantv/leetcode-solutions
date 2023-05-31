# Contiguous array

[Problem link](https://leetcode.com/problems/contiguous-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/contiguous-array

class Solution {
 public:
  int findMaxLength(vector<int>& nums) {
    map<int, int> first = {{0, -1}};

    int best = 0;
    for (int i = 0, cum = 0; i < nums.size(); i++) {
      cum += (2 * nums[i] - 1);
      if (first.count(cum))
        best = max(best, i - first[cum]);
      else
        first[cum] = i;
    }
    return best;
  }
};
```
## Tags

* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
* [Hashmap](/README.md#Hashmap)
