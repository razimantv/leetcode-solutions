# Bitwise xor of all pairings

[Problem link](https://leetcode.com/problems/bitwise-xor-of-all-pairings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution {
 public:
  int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
    int ret = 0;
    if (nums1.size() & 1)
      ret ^= accumulate(nums2.begin(), nums2.end(), 0, bit_xor<int>());
    if (nums2.size() & 1)
      ret ^= accumulate(nums1.begin(), nums1.end(), 0, bit_xor<int>());
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
* [Mathematics](/README.md#Mathematics) > [Composition of operations](/README.md#Mathematics-Composition_of_operations)
