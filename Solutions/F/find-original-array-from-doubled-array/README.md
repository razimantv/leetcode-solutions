# Find original array from doubled array

[Problem link](https://leetcode.com/problems/find-original-array-from-doubled-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution {
 public:
  vector<int> findOriginalArray(vector<int>& changed) {
    multiset<int> seen(changed.begin(), changed.end());
    vector<int> ret;

    while (!seen.empty()) {
      int x = *seen.begin();
      seen.erase(seen.begin());

      auto sit = seen.find(2 * x);
      if (sit == seen.end()) return {};
      ret.push_back(x);
      seen.erase(sit);
    }
    return ret;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
