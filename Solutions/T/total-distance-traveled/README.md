# Total distance traveled

[Problem link](https://leetcode.com/problems/total-distance-traveled/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/total-distance-traveled/

class Solution {
 public:
  int distanceTraveled(int main, int additional) {
    int ret{};
    while (main) {
      if (main < 5) {
        ret += main * 10;
        main = 0;
      } else {
        ret += 50;
        main -= 5;
        if (additional) ++main, --additional;
      }
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
