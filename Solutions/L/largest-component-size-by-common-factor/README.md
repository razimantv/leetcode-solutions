# Largest component size by common factor

[Problem link](https://leetcode.com/problems/largest-component-size-by-common-factor)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-component-size-by-common-factor

class Solution {
  unordered_map<int, int> par;
  int getparent(int u) {
    if (!par.count(u)) return par[u] = u;
    return par[u] == u ? u : (par[u] = getparent(par[u]));
  }

 public:
  int largestComponentSize(vector<int>& A) {
    int Amax = *max_element(A.begin(), A.end());

    vector<int> aprime(Amax + 1);
    for (int i = 2; i * i <= Amax; ++i) {
      if (aprime[i]) continue;
      for (int j = i * i; j <= Amax; j += i) aprime[j] = i;
    }

    for (auto n : A) {
      int next = aprime[n] == 0 ? n : aprime[n], u = getparent(next),
          ncopy = n / next;
      while (ncopy > 1) {
        next = aprime[ncopy] == 0 ? ncopy : aprime[ncopy];
        int v = getparent(next);
        if (v != u) par[v] = u;
        ncopy /= next;
      }
    }

    unordered_map<int, int> cnt;
    int best = 0;
    for (int n : A) {
      best = max(best, ++cnt[getparent(aprime[n] ? aprime[n] : n)]);
    }
    return best;
  }
};
```
## Tags

* [Disjoint set union](/README.md#Disjoint_set_union)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Prime sieving](/README.md#Mathematics-Number_theory-Prime_sieving)
