# Minimum index of a valid split

[Problem link](https://leetcode.com/problems/minimum-index-of-a-valid-split/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

class Solution {
 public:
  int minimumIndex(vector<int>& nums) {
    int n = nums.size();
    vector<int> right(n, -1);
    {
      unordered_map<int, int> freq;
      int best = -1, bestcnt = 0;
      for (int i = n - 1; i > 0; --i) {
        if (++freq[nums[i]] > bestcnt) best = nums[i], bestcnt = freq[best];
        if (2 * bestcnt > n - i) right[i] = best;
      }
    }
    {
      unordered_map<int, int> freq;
      int best = -1, bestcnt = 0;
      for (int i = 0; i < n - 1; ++i) {
        if (++freq[nums[i]] > bestcnt) best = nums[i], bestcnt = freq[best];
        if (2 * bestcnt > i + 1 and right[i + 1] == best) return i;
      }
    }
    return -1;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
* [Majority element](/Collections/majority-element.md#majority-element)
