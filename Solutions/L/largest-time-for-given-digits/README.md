# Largest time for given digits

[Problem link](https://leetcode.com/problems/largest-time-for-given-digits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-time-for-given-digits

class Solution {
 public:
  string largestTimeFromDigits(vector<int>& A) {
    sort(A.begin(), A.end());
    string best = "";
    do {
      int H = A[0] * 10 + A[1], M = A[2] * 10 + A[3];
      if (H > 23 or M > 59) continue;
      string cur = (H < 10 ? "0" : "") + to_string(H) + ":" +
                   (M < 10 ? "0" : "") + to_string(M);
      best = max(best, cur);
    } while (next_permutation(A.begin(), A.end()));
    return best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
