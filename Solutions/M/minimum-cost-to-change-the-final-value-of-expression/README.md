# Minimum cost to change the final value of expression

[Problem link](https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression

pair<int, int> get(const string& str, const vector<int>& match, int l, int r) {
  if (l == r) return {str[l] - '0', 1};
  if (str[r] == ')' and match[r] == l) return get(str, match, l + 1, r - 1);

  int lval, lmin, rval, rmin;
  char op;
  if (str[r] == ')') {
    tie(rval, rmin) = get(str, match, match[r] + 1, r - 1);
    tie(lval, lmin) = get(str, match, l, match[r] - 2);
    op = str[match[r] - 1];
  } else {
    tie(rval, rmin) = get(str, match, r, r);
    tie(lval, lmin) = get(str, match, l, r - 2);
    op = str[r - 1];
  }

  int val, minflip;
  if (op == '|') {
    if ((val = lval | rval)) {  // Need to turn 1 to 0
      minflip = (lval != rval) ? 1 : (1 + min(lmin, rmin));
    } else {  // To turn 0 to 1
      minflip = min(lmin, rmin);
    }
  } else {
    if ((val = lval & rval)) {  // Need to turn 1 to 0: 11
      minflip = min(lmin, rmin);
    } else {  // Need to turn 0 to 1
      minflip = (lval != rval) ? 1 : (1 + min(lmin, rmin));
    }
  }
  return {val, minflip};
}

class Solution {
 public:
  int minOperationsToFlip(string expression) {
    int N = expression.size();
    vector<int> match(N), stack;
    for (int i = 0; i < N; ++i) {
      if (expression[i] == '(') {
        stack.push_back(i);
      } else if (expression[i] == ')') {
        match[i] = stack.back();
        stack.pop_back();
      }
    }
    return get(expression, match, 0, N - 1).second;
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Numerical operations](/Collections/stack.md#numerical-operations)
* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
