# Solving questions with brainpower

[Problem link](https://leetcode.com/problems/solving-questions-with-brainpower/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution {
 public:
  long long mostPoints(vector<vector<int>>& questions) {
    int n = questions.size();
    vector<long long> best(n + 1);
    for (int i = n - 1; i >= 0; --i)
      best[i] = max(best[i + 1],
                    questions[i][0] + best[min(n, i + questions[i][1] + 1)]);
    return best[0];
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
