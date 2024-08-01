# Minimum time to make rope colorful

[Problem link](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution {
 public:
  int minCost(string colors, vector<int>& time) {
    int answer = 0, sum = time[0], max = time[0];
    for (int i = 1, n = colors.size(); i < n; ++i) {
      if (colors[i] != colors[i - 1]) {
        answer += sum - max;
        sum = max = time[i];
      } else {
        sum += time[i];
        max = std::max(max, time[i]);
      }
    }
    return answer + sum - max;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
