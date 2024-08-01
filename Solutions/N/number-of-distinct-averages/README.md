# Number of distinct averages

[Problem link](https://leetcode.com/problems/number-of-distinct-averages/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-distinct-averages/

class Solution {
 public:
  int distinctAverages(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    unordered_set<int> s;
    for (int i = 0, j = n - 1; i < j; ++i, --j) s.insert(nums[i] + nums[j]);
    return s.size();
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
* [Hashmap](/Collections/hashmap.md#hashmap)
