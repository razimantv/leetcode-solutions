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

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
