# Count palindromic subsequences

[Problem link](https://leetcode.com/problems/count-palindromic-subsequences/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-palindromic-subsequences/

class Solution {
 public:
  int countPalindromes(string s) {
    int n = s.size();
    vector<pair<array<int, 10>, array<int, 100>>> left(n), right(n);
    for (int i = 0; i < n; ++i) {
      if (i) left[i] = left[i - 1];
      int c = s[i] - '0';
      for (int prev = 0; prev < 10; ++prev)
        left[i].second[prev * 10 + c] += left[i].first[prev];
      left[i].first[c]++;
    }
    for (int i = n - 1; i >= 0; --i) {
      if (i < n - 1) right[i] = right[i + 1];
      int c = s[i] - '0';
      for (int prev = 0; prev < 10; ++prev)
        right[i].second[prev * 10 + c] += right[i].first[prev];
      right[i].first[c]++;
    }

    long long ret{};
    for (int pref = 0; pref < 100; ++pref)
      for (int i = 2; i + 2 < n; ++i)
        ret += left[i - 1].second[pref] * (long long)right[i + 1].second[pref];

    return ret % 1'000'000'007;
  }
};
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [From both ends of array](/README.md#Array_scanning-From_both_ends_of_array)
* [Palindrome](/README.md#Palindrome)
* [Dynamic programming](/README.md#Dynamic_programming)
