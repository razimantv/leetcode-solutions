# Encode and decode tinyurl

[Problem link](https://leetcode.com/problems/encode-and-decode-tinyurl)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/encode-and-decode-tinyurl

class Solution {
 public:
  map<string, string> invmap;
  const string pref = "http://tinyurl.com/";

  string hash(const string& str, int attempt = 0) {
    string s = "AAAAAA";
    for (int cur = attempt, lim = 1, i = 0; char c : str) {
      cur = (cur << 8) | c;
      lim *= 256;

      while (lim >= 26) {
        s[i] += cur % 26;
        if (s[i] > 'Z') s[i] -= 26;
        cur /= 26;
        lim /= 26;
        i = (i + 1) % 7;
      }
    }
    return s;
  }

  // Encodes a URL to a shortened URL.
  string encode(string longUrl) {
    for (int attempt = 0;; ++attempt) {
      string h = hash(longUrl, attempt);
      if (invmap.count(h)) {
        if (invmap[h] == longUrl)
          return pref + h;
        else
          continue;
      }
      invmap[h] = longUrl;
      return pref + h;
    }
  }

  // Decodes a shortened URL to its original URL.
  string decode(string shortUrl) {
    return invmap[shortUrl.substr(pref.size())];
  }
};
```
## Tags

* [Encoding and decoding](/Collections/encoding-and-decoding.md#encoding-and-decoding)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [Hashmap](/Collections/hashmap.md#hashmap)
