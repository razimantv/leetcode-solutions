# Asteroid collision

[Problem link](https://leetcode.com/problems/asteroid-collision)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/asteroid-collision

class Solution {
 public:
  vector<int> asteroidCollision(vector<int>& asteroids) {
    vector<int> ret;
    for (int x : asteroids) {
      if (x > 0)
        ret.push_back(x);
      else {
        while (1) {
          if (ret.empty() or ret.back() < 0) {
            ret.push_back(x);
            break;
          } else if (ret.back() > -x)
            break;
          else if (ret.back() == -x) {
            ret.pop_back();
            break;
          } else
            ret.pop_back();
        }
      }
    }
    return ret;
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [From array elements](/Collections/stack.md#from-array-elements)
