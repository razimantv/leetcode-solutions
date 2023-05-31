# Successful pairs of spells and potions

[Problem link](https://leetcode.com/problems/successful-pairs-of-spells-and-potions)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions

class Solution {
 public:
  vector<int> successfulPairs(vector<int>& spells, vector<int>& portions,
                              long long success) {
    sort(portions.begin(), portions.end());
    vector<int> ret;
    for (int s : spells) {
      long long pp = (success + s - 1) / s;
      int p = (pp >= INT_MAX) ? INT_MAX : pp;
      ret.push_back(portions.end() -
                    lower_bound(portions.begin(), portions.end(), p));
    }
    return ret;
  }
};
```