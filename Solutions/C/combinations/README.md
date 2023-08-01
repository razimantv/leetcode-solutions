# Combinations

[Problem link](https://leetcode.com/problems/combinations/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/combinations/

class Solution {
 public:
  // ChatGPT solution
  vector<vector<int>> combine(int n, int k) {
    std::vector<std::vector<int>> result;
    std::vector<int> currentCombination;
    backtrack(result, currentCombination, 1, n, k);
    return result;
  }

  void backtrack(std::vector<std::vector<int>>& result,
                 std::vector<int>& currentCombination, int start, int n,
                 int k) {
    if (currentCombination.size() == k) {
      result.push_back(currentCombination);
      return;
    }

    for (int i = start; i <= n; i++) {
      currentCombination.push_back(i);
      backtrack(result, currentCombination, i + 1, n, k);
      currentCombination.pop_back();
    }
  }
};
```
## Tags

* [Backtracking](/README.md#Backtracking) > [Push and pop for efficient state update](/README.md#Backtracking-Push_and_pop_for_efficient_state_update)
* [ChatGPT](/README.md#ChatGPT)
