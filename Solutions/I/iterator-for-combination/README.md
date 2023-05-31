# Iterator for combination

[Problem link](https://leetcode.com/problems/iterator-for-combination)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/iterator-for-combination

class CombinationIterator {
 public:
  vector<int> perm;
  bool can;
  string word;
  CombinationIterator(string characters, int k) {
    word = characters;
    perm = vector<int>(word.size(), 0);
    fill(perm.begin(), perm.begin() + k, 1);
    can = true;
  }

  string next() {
    string ret = "";
    for (int i = 0; i < perm.size(); ++i)
      if (perm[i]) ret += word[i];
    can = prev_permutation(perm.begin(), perm.end());
    return ret;
  }

  bool hasNext() { return can; }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters,
 * combinationLength); string param_1 = obj->next(); bool param_2 =
 * obj->hasNext();
 */
```
## Tags

* [Design data structure](/README.md#Design_data_structure)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Brute force enumeration](/README.md#Brute_force_enumeration) > [Combinatorial](/README.md#Brute_force_enumeration-Combinatorial)
