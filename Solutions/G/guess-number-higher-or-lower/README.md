# Guess number higher or lower

[Problem link](https://leetcode.com/problems/guess-number-higher-or-lower)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/guess-number-higher-or-lower

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
 public:
  int guessNumber(int r, long long l = 0) {
    while (r - l > 1) {
      auto m = (r + l) >> 1;
      int x = guess(m);
      if (x == 0)
        return m;
      else if (x == -1)
        r = m;
      else
        l = m;
    }
    return r;
  }
};
```
## Tags

* [Binary search](/README.md#Binary_search)
