# Find score of an array after marking all elements

[Problem link](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

class Solution {
 public:
  long long findScore(vector<int>& nums) {
    int n = nums.size();
    vector<int> mark(n);

    auto cmp = [&](int i, int j) {
      if (nums[i] != nums[j]) return nums[i] < nums[j];
      return i < j;
    };

    vector<int> idx(n);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(), cmp);

    long long ret{};
    for (int x : idx) {
      if (mark[x]) continue;
      mark[x] = 1;
      if (x) mark[x - 1] = 1;
      if (x < n - 1) mark[x + 1] = 1;
      ret += nums[x];
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
