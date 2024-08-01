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

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
