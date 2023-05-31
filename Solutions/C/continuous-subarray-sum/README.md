# Continuous subarray sum

[Problem link](https://leetcode.com/problems/continuous-subarray-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/continuous-subarray-sum/

class Solution {
 public:
  bool checkSubarraySum(vector<int>& nums, int k) {
    unordered_set<long long> seen;
    long long prev{}, cur{};
    for (int x : nums) {
      cur = (cur + x) % k;
      if (seen.count(cur)) return true;
      seen.insert(prev);
      prev = cur;
    }
    return false;
  }
};
```
## Tags

* [Hashmap](/README.md#Hashmap)
* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
