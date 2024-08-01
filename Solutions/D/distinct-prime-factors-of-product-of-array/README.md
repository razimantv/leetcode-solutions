# Distinct prime factors of product of array

[Problem link](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution {
 public:
  int distinctPrimeFactors(vector<int>& nums) {
    vector<vector<int>> primes(1001);
    for (int i = 2; i < 1001; ++i) {
      if (primes[i].size()) continue;
      for (int j = i; j < 1001; j += i) primes[j].push_back(i);
    }

    unordered_set<int> all;
    for (int x : nums)
      for (int p : primes[x]) all.insert(p);
    return all.size();
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Prime sieving](/Collections/mathematics.md#prime-sieving)
* [Hashmap](/Collections/hashmap.md#hashmap)
