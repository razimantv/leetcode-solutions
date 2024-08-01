# Minimum absolute difference

[Problem link](https://leetcode.com/problems/minimum-absolute-difference)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-absolute-difference

class Solution {
 public:
  vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
    sort(arr.begin(), arr.end());
    vector<vector<int>> ret;
    for (int i = 1, n = arr.size(); i < n; ++i) {
      if (ret.empty() or ret.back()[1] - ret.back()[0] > arr[i] - arr[i - 1]) {
        ret.clear();
        ret.push_back({arr[i - 1], arr[i]});
      } else if (ret.back()[1] - ret.back()[0] == arr[i] - arr[i - 1])
        ret.push_back({arr[i - 1], arr[i]});
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
