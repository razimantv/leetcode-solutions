# Count the number of beautiful subarrays

[Problem link](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

class Solution {
 public:
  long long beautifulSubarrays(vector<int>& nums) {
    unordered_map<int, int> cnt;
    cnt[0] = 1;
    long long ret{};
    for (int i = 0, n = nums.size(), pref = 0; i < n; ++i)
      ret += cnt[pref ^= nums[i]]++;
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
* [Hashmap](/README.md#Hashmap)
