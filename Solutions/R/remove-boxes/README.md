# Remove boxes

[Problem link](https://leetcode.com/problems/remove-boxes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-boxes

class Solution {
 public:
  int cache[101][101][101];
  int removeBoxes(const vector<int>& boxes, int i = 0, int j = -1, int k = 0) {
    if (j == -1) j = boxes.size() - 1;
    if (j < i)
      return 0;
    else if (cache[i][j][k])
      return cache[i][j][k];

    cache[i][j][k] = (k + 1) * (k + 1) + removeBoxes(boxes, i + 1, j, 0);
    for (int ii = i + 1; ii <= j; ++ii)
      if (boxes[ii] == boxes[i])
        cache[i][j][k] =
            max(cache[i][j][k], removeBoxes(boxes, i + 1, ii - 1, 0) +
                                    removeBoxes(boxes, ii, j, k + 1));
    return cache[i][j][k];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
