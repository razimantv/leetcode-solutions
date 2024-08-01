# Range product queries of powers

[Problem link](https://leetcode.com/problems/range-product-queries-of-powers/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/range-product-queries-of-powers/

class Solution {
 public:
  vector<int> productQueries(int n, vector<vector<int>>& queries) {
    vector<int> powers;
    for (int i = 1; n; i <<= 1) {
      if (n & i) {
        powers.push_back(i);
        n ^= i;
      }
    }

    const long long MOD = 1'000'000'007ll;
    int Q = queries.size();
    vector<int> ret(Q, 1);
    for (int i = 0; i < Q; ++i) {
      int l = queries[i][0], r = queries[i][1];
      for (int j = l; j <= r; ++j) {
        ret[i] = (ret[i] * (long long)powers[j]) % MOD;
      }
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
