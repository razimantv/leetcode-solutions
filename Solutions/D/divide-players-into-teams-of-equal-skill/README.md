# Divide players into teams of equal skill

[Problem link](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/divide-players-into-teams-of-equal-skill

class Solution {
 public:
  long long dividePlayers(vector<int>& skills) {
    sort(skills.begin(), skills.end());
    int team = skills[0] + skills.back();
    long long ret{};
    for (int i = 0, j = skills.size() - 1; i < j; ++i, --j) {
      if (skills[i] + skills[j] != team) return -1;
      ret += skills[i] * skills[j];
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
