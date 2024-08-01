# Implement rand10 using rand7

[Problem link](https://leetcode.com/problems/implement-rand10-using-rand7)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/implement-rand10-using-rand7

// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
 public:
  vector<int> hist;
  int rand10() {
    if (hist.empty()) hist = {1, 0};

    while (1) {
      int cur = rand7() - 1;
      hist[0] *= 7;
      hist[1] = hist[1] * 7 + cur;

      if (hist[0] > 9) {
        int lim = (hist[0] / 10) * 10;
        if (hist[1] >= lim) {
          hist[0] %= 10;
          hist[1] %= 10;
        } else {
          lim /= 10;
          int ret = hist[1] / lim + 1;
          hist[0] = lim;
          hist[1] %= lim;
          return ret;
        }
      }
    }

    return 0;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Probability](/Collections/mathematics.md#probability)
