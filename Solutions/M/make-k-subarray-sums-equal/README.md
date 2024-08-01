# Make k subarray sums equal

[Problem link](https://leetcode.com/problems/make-k-subarray-sums-equal/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/make-k-subarray-sums-equal/

class Solution {
 public:
  long long work(vector<int> ar, int n) {
    int x = n / 2;
    nth_element(ar.begin(), ar.begin() + x, ar.end());
    long long ret{};
    for (int y : ar) ret += abs(y - ar[x]);
    return ret;
  }
  long long makeSubKSumEqual(vector<int>& arr, int k) {
    int n = arr.size(), g = __gcd(n, k);
    long long ret{};
    for (int i = 0; i < g; ++i) {
      vector<int> temp;
      for (int j = i; j < n; j += g) temp.push_back(arr[j]);
      ret += work(temp, n / g);
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Sorting](/Collections/sorting.md#sorting) > [Partial](/Collections/sorting.md#partial)
