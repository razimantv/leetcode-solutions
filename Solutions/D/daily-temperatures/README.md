# Daily temperatures

[Problem link](https://leetcode.com/problems/daily-temperatures)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/daily-temperatures

class Solution {
 public:
  vector<int> dailyTemperatures(vector<int>& temperatures) {
    int N = temperatures.size();
    vector<int> stk, ans(N);

    for (int i = N - 1; i >= 0; --i) {
      while (!stk.empty() and temperatures[stk.back()] <= temperatures[i])
        stk.pop_back();
      if (stk.empty())
        ans[i] = 0;
      else
        ans[i] = stk.back() - i;
      stk.push_back(i);
    }
    return ans;
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
