# Find the prefix common array of two arrays

[Problem link](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution {
 public:
  vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
    unordered_map<int, int> cnt;
    vector<int> ret;
    for (int i = 0, n = A.size(), cur = 0; i < n; ++i) {
      for (int x : {A[i], B[i]})
        if (!(cnt[x] ^= 1)) ++cur;
      ret.push_back(cur);
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
