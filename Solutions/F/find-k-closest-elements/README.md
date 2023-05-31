# Find k closest elements

[Problem link](https://leetcode.com/problems/find-k-closest-elements)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-k-closest-elements

class Solution {
  bool cmp(int a, int b, int x) {
    int A = abs(a - x), B = abs(b - x);
    if (A != B)
      return A < B;
    else
      return a < b;
  }

 public:
  vector<int> findClosestElements(vector<int>& arr, int k, int x) {
    int n = arr.size();
    if (k == n) return arr;

    int i = lower_bound(arr.begin(), arr.end(), x) - arr.begin();
    if (i == n or (i and cmp(arr[i - 1], arr[i], x))) --i;
    int j = i;
    while (j - i + 1 < k) {
      if (j == n - 1 or (i and cmp(arr[i - 1], arr[j + 1], x)))
        --i;
      else
        ++j;
    }

    arr.erase(arr.begin(), arr.begin() + i);
    arr.erase(arr.begin() + k, arr.end());
    return arr;
  }
};
```
## Tags

* [Binary search](/README.md#Binary_search)
* [Two pointers](/README.md#Two_pointers)
