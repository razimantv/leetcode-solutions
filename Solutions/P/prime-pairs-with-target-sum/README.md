# Prime pairs with target sum

[Problem link](https://leetcode.com/problems/prime-pairs-with-target-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/prime-pairs-with-target-sum/

class Solution {
 public:
  vector<vector<int>> findPrimePairs(int n) {
    vector<char> notprime(n + 1);
    for (int i = 2; i * i <= n; ++i) {
      if (notprime[i]) continue;
      for (int j = i * i; j <= n; j += i) notprime[j] = 1;
    }

    vector<vector<int>> ret;
    for (int i = 2, j = n - 2; i <= j; ++i, --j)
      if (!notprime[i] and !notprime[j]) ret.push_back({i, j});
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Prime sieving](/Collections/mathematics.md#prime-sieving)
