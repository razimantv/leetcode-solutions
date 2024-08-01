# Largest number

[Problem link](https://leetcode.com/problems/largest-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-number

class Solution {
 public:
  string largestNumber(vector<int>& nums) {
    int N = nums.size();
    vector<string> vs(N);
    for (int i = 0; i < N; ++i) vs[i] = to_string(nums[i]);
    sort(vs.begin(), vs.end(), [](const string& s1, const string& s2) -> bool {
      return (s2 + s1) < (s1 + s2);
    });

    string ret{};
    for (const string& s : vs) {
      if (ret == "0") ret = "";
      ret += s;
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Greedy](/Collections/greedy.md#greedy)
