# Apply operations to maximize score

[Problem link](https://leetcode.com/problems/apply-operations-to-maximize-score/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/apply-operations-to-maximize-score/

class Solution {
 public:
  static vector<int> score;
  void init() {
    const int NMAX = 100'001;
    score.resize(NMAX);
    for (int i = 2; i < NMAX; ++i) {
      if (score[i]) continue;
      for (int j = i; j < NMAX; j += i) ++score[j];
    }
  }

  void modpow(long long& start, long long n, long long k, long long MOD) {
    while (k) {
      if (k & 1) start = (start * n) % MOD;
      n = (n * n) % MOD;
      k >>= 1;
    }
  }
  int maximumScore(vector<int>& nums, long long k) {
    if (score.empty()) init();
    int n = nums.size();
    vector<int> left(n, 0), right(n, n - 1), indices(n);
    vector<pair<int, int>> mono;
    for (int i = 0; i < n; ++i) {
      int si = score[nums[i]];
      while (!mono.empty()) {
        auto [j, sj] = mono.back();
        if (sj >= si) {
          left[i] = j + 1;
          break;
        }
        right[j] = i - 1;
        mono.pop_back();
      }
      mono.push_back({i, si});
    }
    iota(indices.begin(), indices.end(), 0);
    sort(indices.begin(), indices.end(),
         [&](int i, int j) { return nums[i] > nums[j]; });

    long long ret{1ll};
    for (int i : indices) {
      long long poss = (i - left[i] + 1ll) * (right[i] - i + 1);
      modpow(ret, nums[i], min(poss, k), 1'000'000'007);
      if ((k -= poss) <= 0) break;
    }
    return ret;
  }
};

vector<int> Solution::score = {};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Prime sieving](/README.md#Mathematics-Number_theory-Prime_sieving)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Modular exponentiation/inverse](/README.md#Mathematics-Number_theory-Modular_exponentiation_inverse)
* [Stack](/README.md#Stack) > [Monotonic stack](/README.md#Stack-Monotonic_stack)
* [Sorting](/README.md#Sorting) > [Index array](/README.md#Sorting-Index_array)
* [Greedy](/README.md#Greedy)
