# Bulls and cows

[Problem link](https://leetcode.com/problems/bulls-and-cows)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/bulls-and-cows

class Solution {
 public:
  string getHint(string secret, string guess) {
    int excess[10] = {0}, bulls = 0, cows = 0, N = secret.size();
    for (int i = 0; i < N; i++) {
      if (secret[i] == guess[i])
        ++bulls;
      else {
        if (excess[secret[i] - '0']++ < 0) ++cows;
        if (excess[guess[i] - '0']-- > 0) ++cows;
      }
    }
    return to_string(bulls) + "A" + to_string(cows) + "B";
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
