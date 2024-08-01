# Advantage shuffle

[Problem link](https://leetcode.com/problems/advantage-shuffle)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/advantage-shuffle

class Solution {
 public:
  vector<int> advantageCount(vector<int>& A, vector<int>& B) {
    int N = A.size();
    vector<int> indices(N), discard, ret(N);
    iota(indices.begin(), indices.end(), 0);
    sort(indices.begin(), indices.end(),
         [&B](int i, int j) { return B[i] < B[j]; });
    sort(A.begin(), A.end(), greater<int>());

    for (int i : indices) {
      while (!A.empty() and A.back() <= B[i]) {
        discard.push_back(A.back());
        A.pop_back();
      }
      vector<int>& cur = A.empty() ? discard : A;
      ret[i] = cur.back();
      cur.pop_back();
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Greedy](/Collections/greedy.md#greedy)
