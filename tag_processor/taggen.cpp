#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>

int main() {
  using namespace std::filesystem;
  current_path("../Solutions");

  std::map<std::string, std::set<std::pair<std::string, std::string>>>
      tagmap;
  for (auto const& collection : directory_iterator{"."}) {
    if (!is_directory(collection)) continue;
    for (auto const& problem : directory_iterator{collection}) {
      if (!is_directory(problem)) continue;
      std::string problemname = path(problem).filename();
      std::string problempath =
          path(collection).filename() / path(problem).filename();
      for (char& c : problemname)
        if (c == '-') c = ' ';
      problemname[0] = toupper(problemname[0]);
      if (!exists(path(problem) / "tags")) {
        tagmap["Untagged"].insert({problemname, problempath});
        continue;
      }
      std::ifstream tagsfile(path(path(problem) / "tags"));
      for (std::string tag; getline(tagsfile, tag);) {
        tagmap[tag].insert({problemname, problempath});
      }
    }
  }

  std::cout << "\n# Problems by tags (INCOMPLETE!)\n";
  std::vector<std::string> prevtaghierarchy;
  for (auto& [tag, problemlist] : tagmap) {
    if (tag == "Untagged") continue;
    std::istringstream iss(tag);
    std::vector<std::string> taghierarchy;
    std::string token;
    while (std::getline(iss, token, '>')) {
      taghierarchy.push_back(token);
    }
    int level = 0;
    for(auto& token: prevtaghierarchy) {
      if (level == taghierarchy.size() or token != taghierarchy[level]) break;
      ++level;
    }
    while(level < taghierarchy.size()) {
      std::cout << "\n"
                << std::string(level + 2, '#') << " " << taghierarchy[level]
                << "\n";
      ++level;
    }

    for (auto& [name, path] : problemlist) {
      std::cout << "* [" << name << "](Solutions/" << path << ")\n";
    }
    prevtaghierarchy = taghierarchy;
  }
  std::cout << "\n## Untagged\n";
  for (auto& [name, path] : tagmap["Untagged"]) {
    std::cout << "* [" << name << "](Solutions/" << path << ")\n";
    }
  return 0;
}
