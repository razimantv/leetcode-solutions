# Invalid transactions

[Problem link](https://leetcode.com/problems/invalid-transactions/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/invalid-transactions/

class Solution {
 public:
  typedef tuple<string, int, int, string, int> transaction;

  static string get_str(string str, int& pos) {
    string ret;
    while (isalpha(str[pos])) ret += str[pos++];
    if (str[pos]) ++pos;
    return ret;
  }

  static int get_int(string str, int& pos) {
    int ret{};
    while (isdigit(str[pos])) ret = ret * 10 + str[pos++] - '0';
    if (str[pos]) ++pos;
    return ret;
  }

  static transaction parse(const std::string& str, int id) {
    int pos = 0;
    string name = get_str(str, pos);
    int time = get_int(str, pos);
    int value = get_int(str, pos);
    string city = get_str(str, pos);

    return {name, time, value, city, id};
  }

  vector<string> invalidTransactions(vector<string>& transactions) {
    int n = transactions.size();
    vector<transaction> parsed(n);
    for (int i = 0; i < n; ++i) parsed[i] = parse(transactions[i], i);
    sort(parsed.begin(), parsed.end());

    // To do range updates using prefix sum
    // When we identify a range [j, i] as bad,
    //    increment badness[j] and decrement badness[i+1]
    // On taking prefix sum, this will increment every element in [j, i] by 1
    vector<int> badness(n + 1);

    // Active cities for current user:
    //    Where a transaction occured in last 60 minutes
    //    map: city -> count of transactions
    unordered_map<string, int> active_cities;

    // Sliding window from j to i:
    //    active transactions (last 60 minutes) for current user
    for (int i = 0, j = 0; i < n; ++i) {
      const auto& [name, time, value, city, id] = parsed[i];

      // If the  user changed, reset active city
      if (i and name != get<0>(parsed[i - 1])) {
        j = i;
        active_cities.clear();
      }

      ++active_cities[city];

      // If value is above threshold, [i, i] is a bad range
      if (value > 1000) ++badness[i], --badness[i + 1];

      // Sliding window update:
      //    Decrement count of cities if they go outside active window
      //    If count becomes 0, remove it from hashmap
      while (get<1>(parsed[j]) < time - 60) {
        const auto& prevcity = get<3>(parsed[j]);
        if (--active_cities[prevcity] == 0) active_cities.erase(prevcity);
        ++j;
      }

      // If active city count > 1, range of transactions [j, i] are all invalid
      if (active_cities.size() > 1) ++badness[j], --badness[i + 1];
    }

    vector<string> ret;
    // Take prefix sum of badness array
    // Transaction is invalid iff prefix sum > 0
    for (int i = 0, badness_pref = 0; i < n; ++i) {
      if (badness_pref += badness[i])
        ret.push_back(transactions[get<4>(parsed[i])]);
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Remembering index](/Collections/sorting.md#remembering-index)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
* [Hashmap](/Collections/hashmap.md#hashmap)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [For range updates](/Collections/prefix.md#for-range-updates)
* [Range updates using prefix sum](/Collections/range-updates-using-prefix-sum.md#range-updates-using-prefix-sum)
* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
