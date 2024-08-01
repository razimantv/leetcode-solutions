# Maximum nesting depth of two valid parentheses strings

[Problem link](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings

class Solution {
 public:
  vector<int> maxDepthAfterSplit(string seq) {
    vector<int> ret;
    int prefix = 0;
    for (char c : seq) ret.push_back((c == '(' ? prefix++ : --prefix) & 1);
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
