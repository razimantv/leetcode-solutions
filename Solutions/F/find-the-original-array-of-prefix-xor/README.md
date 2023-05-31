# Find the original array of prefix xor

[Problem link](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution {
 public:
  vector<int> findArray(vector<int>& pref) {
    int n = pref.size();
    for (int i = n - 1; i; --i) pref[i] ^= pref[i - 1];
    return pref;
  }
};
```
## Tags

* [Bitwise operation](/README.md#Bitwise_operation) > [Self-inverse property of xor](/README.md#Bitwise_operation-Self_inverse_property_of_xor)
* [Array scanning](/README.md#Array_scanning) > [Right to left](/README.md#Array_scanning-Right_to_left)
