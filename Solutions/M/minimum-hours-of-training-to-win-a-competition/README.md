# Minimum hours of training to win a competition

[Problem link](https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition

class Solution {
 public:
  int minNumberOfHours(int initE, int initX, vector<int>& energy,
                       vector<int>& experience) {
    int n = energy.size();
    int minE = initE, minX = initX;
    for (int i = 0; i < n; ++i) {
      initE -= energy[i];
      initX -= experience[i];
      minE = min(minE, initE);
      minX = min(minX, initX);
      initX += 2 * experience[i];
    }

    return max(0, 1 - minE) + max(0, 1 - minX);
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
