#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>

typedef std::vector<std::string> Tag;
typedef std::pair<std::string, std::string> Problem;

Tag taghierarchy(std::string tag_str) {
  std::istringstream iss(tag_str);
  Tag ret;
  std::string token;
  while (std::getline(iss, token, '>')) ret.push_back(token);
  return ret;
}

std::string sanitize(std::string str) {
  for (char& c : str)
    if (!isalnum(c)) c = '_';
  return str;
}

std::string readmetagline(Tag& tag) {
  std::string ret, taglabel;
  for (auto t : tag) {
    if (!ret.empty()) {
      ret += " > ";
      taglabel += "-";
    }
    taglabel += sanitize(t);
    ret += "[" + t + "](/README.md#" + taglabel + ")";
  }
  return ret;
}

int main() {
  using namespace std::filesystem;
  current_path("../Solutions");

  std::map<Tag, std::set<Problem>> tagmap;
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
      if (exists(path(problem) / "README.md.base"))
        copy_file(path(problem) / "README.md.base", path(problem) / "README.md",
                  std::filesystem::copy_options::overwrite_existing);

      if (!exists(path(problem) / "tags")) {
        tagmap[{"Untagged"}].insert({problemname, problempath});
        continue;
      }
      std::ifstream tagsfile(path(path(problem) / "tags"));
      std::ofstream readme(path(path(problem) / "README.md"), std::ios::app);
      readme << "\n## Tags\n\n";
      for (std::string tag_str; getline(tagsfile, tag_str);) {
        auto tag = taghierarchy(tag_str);
        tagmap[tag].insert({problemname, problempath});
        readme << "* " << readmetagline(tag) << "\n";
      }
    }
  }

  std::cout << "\n# Problems by tags (INCOMPLETE!)\n";
  std::vector<std::string> prevtag;
  for (auto& [tag, problemlist] : tagmap) {
    if (tag[0] == "Untagged") continue;
    int level = 0;
    std::string taglabel;
    for (auto& token : prevtag) {
      if (level == tag.size() or token != tag[level]) break;
      if (!taglabel.empty()) taglabel += '-';
      taglabel += sanitize(tag[level]);
      ++level;
    }
    while (level < tag.size()) {
      if (!taglabel.empty()) taglabel += '-';
      taglabel += sanitize(tag[level]);
      std::cout << "\n"
                << std::string(level + 2, '#') << " "
                << "<a name=\"" << taglabel << "\">" << tag[level] << "</a>\n";
      ++level;
    }

    for (auto& [name, path] : problemlist) {
      std::cout << "* [" << name << "](Solutions/" << path << ")\n";
    }
    prevtag = tag;
  }
  std::cout << "\n## Untagged\n";
  for (auto& [name, path] : tagmap[{"Untagged"}]) {
    std::cout << "* [" << name << "](Solutions/" << path << ")\n";
  }
  return 0;
}
