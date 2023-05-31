# Count unique characters of all substrings of a given string

[Problem link](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string

class Solution {
 public:
  int uniqueLetterString(string s) {
    int N = s.size();
    vector<int> current(26, -1), previous(26, -1);
    long long ret{};
    for (int i = 0; i < N; ++i) {
      int c = s[i] - 'A';
      previous[c] = current[c];
      current[c] = i;
      for (int i = 0; i < 26; ++i) ret += current[i] - previous[i];
    }
    return ret;
  }
};
```
## Tags

* [Unique elements in subarray](/README.md#Unique_elements_in_subarray)
* [Array scanning](/README.md#Array_scanning) > [Location of previous element with same value](/README.md#Array_scanning-Location_of_previous_element_with_same_value)
* [Dynamic programming](/README.md#Dynamic_programming)
