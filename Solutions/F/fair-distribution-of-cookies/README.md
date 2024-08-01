# Fair distribution of cookies

[Problem link](https://leetcode.com/problems/fair-distribution-of-cookies)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/fair-distribution-of-cookies

class Solution {
 public:
  int distributeCookies(vector<int>& cookies, int k) {
    sort(cookies.begin(), cookies.end(), greater<int>());
    int n = cookies.size(), pp = 1;
    for (int i = 1; i < n; ++i) pp *= k;

    int ret = INT_MAX;
    for (int i = 0; i < pp; ++i) {
      vector<int> v(k);
      int worst = v[0] = cookies[0];
      for (int ii = i, j = 1; j < n; ++j) {
        if ((worst = max(worst, v[ii % k] += cookies[j])) >= ret) goto BPP;
        ii /= k;
      }
      ret = min(ret, worst);
    BPP:;
    }
    return ret;
  }
};
```
## Tags

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
