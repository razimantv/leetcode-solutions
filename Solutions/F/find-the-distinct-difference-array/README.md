# Find the distinct difference array

[Problem link](https://leetcode.com/problems/find-the-distinct-difference-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-distinct-difference-array/

class Solution {
 public:
  vector<int> distinctDifferenceArray(vector<int>& nums) {
    unordered_set<int> lunique, runique;
    int n = nums.size();
    vector<int> ret(n);
    for (int i = 0; i < n; ++i) {
      lunique.insert(nums[i]);
      ret[i] = lunique.size();
    }
    for (int i = n - 1; i >= 0; --i) {
      ret[i] -= runique.size();
      runique.insert(nums[i]);
    }
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
