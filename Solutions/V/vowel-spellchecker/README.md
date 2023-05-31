# Vowel spellchecker

[Problem link](https://leetcode.com/problems/vowel-spellchecker)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/vowel-spellchecker

class Solution {
 public:
  unordered_set<string> words;
  unordered_map<string, string> capital_match, vowel_match;
  const string vowels = "aeiou";

  void small(string& word) {
    for (char& c : word) c = tolower(c);
  }

  void vowel(string& word) {
    for (char& c : word) {
      for (char v : vowels) {
        if (c == v) {
          c = '*';
          break;
        }
      }
    }
  }

  vector<string> spellchecker(vector<string>& wordlist,
                              vector<string>& queries) {
    for (const string& word : wordlist) {
      words.insert(word);
      string temp = word;
      small(temp);
      if (!capital_match.count(temp)) capital_match[temp] = word;
      vowel(temp);
      if (!vowel_match.count(temp)) vowel_match[temp] = word;
    }

    for (string& word : queries) {
      if (words.count(word)) continue;
      small(word);
      if (capital_match.count(word)) {
        word = capital_match[word];
        continue;
      }
      vowel(word);
      if (vowel_match.count(word))
        word = vowel_match[word];
      else
        word = "";
    }

    return queries;
  }
};
```