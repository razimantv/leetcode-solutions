# Find the student that will replace the chalk

[Problem link](https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk

class Solution {
 public:
  int chalkReplacer(vector<int>& chalk, int k) {
    long long tot = 0;
    int n = chalk.size();
    for (int i = 0; i < n; ++i) {
      tot += chalk[i];
      if (tot > k) return i;
    }
    return chalkReplacer(chalk, k % tot);
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
