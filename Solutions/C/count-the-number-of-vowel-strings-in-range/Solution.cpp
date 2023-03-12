// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution {
 public:
  int vowelStrings(vector<string>& words, int left, int right) {
    unordered_set<char> vowels;
    for (char c : "aeiou") vowels.insert(c);
    int ret{};
    for (int i = left; i <= right; ++i)
      if (vowels.count(words[i][0]) and vowels.count(words[i].back())) ++ret;
    return ret;
  }
};
