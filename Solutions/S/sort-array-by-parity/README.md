# Sort array by parity

[Problem link](https://leetcode.com/problems/sort-array-by-parity)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-array-by-parity

class Solution {
 public:
  vector<int> sortArrayByParity(vector<int>& A) {
    for (int i = 0, j = A.size() - 1; i < j;) {
      if (A[i] % 2 == 0)
        ++i;
      else if (A[j] % 2)
        --j;
      else
        swap(A[i++], A[j--]);
    }
    return A;
  }
};
```