#include "utils.hpp"

#include <fmt/core.h>
// #include <range-v3/range/v3/range.hpp>

#include <algorithm>
#include <ranges>
#include <string>
#include <vector>

/*
1 <= operations.length <= 100
operations[i] will be either "++X", "X++", "--X", or "X--".
*/

int finalValueAfterOperations1(std::vector<std::string>& operations) {
  int x = 0;
  for (const std::string& op : operations)
    if (op.compare("++X") == 0 || op.compare("X++") == 0)
      ++x;
    else if (op.compare("--X") == 0 || op.compare("X--") == 0)
      --x;
  return x;
}

int finalValueAfterOperations1b(std::vector<std::string>& operations) {
  int x = 0;
  for (const std::string& op : operations)
    if (op.compare("++X") == 0 || op.compare("X++") == 0)
      ++x;
    else
      --x;
  return x;
}

int finalValueAfterOperations2(std::vector<std::string>& operations) {
  int x = 0;
  for (const std::string& op : operations) {
    if (op[1] == '+')
      ++x;
    else
      --x;
  }
  return x;
}

int finalValueAfterOperations2b(std::vector<std::string>& operations) {
  int x = 0;
  for (const std::string& op : operations)
    x += op[1] == '+' ? 1 : -1;
  return x;
}

// int finalValueAfterOperations3(std::vector<std::string>& ops) {
//   auto opToPlusMinusOne = [](std::string& op) { if (op[1] == '+') return 1; else return -1; };
//   auto ones = ops | std::ranges::views::transform(opToPlusMinusOne);
//   // return std::ranges::fold_left(foo, 0, std::plus<int>());
//   return std::accumulate(ones.begin(), ones.end(), 0);
// }

int main() {
  std::vector<std::string> ops = {"--X", "X--", "++X", "X++"};
  std::vector<std::string> inp = {"--X", "X--", "++X"};
  for (int n : std::ranges::views::iota(0, 10'000))
    inp.insert(inp.end(), ops.begin(), ops.end());

  Timer t;
  int result{};
  int dur{};

  for (int i = 0; i < 10'00; ++i)
    result = finalValueAfterOperations1(inp);
  dur = t.timeSinceLastMs();
  fmt::print("{} {}\n", result, dur);

  for (int i = 0; i < 10'00; ++i)
    result = finalValueAfterOperations1b(inp);
  dur = t.timeSinceLastMs();
  fmt::print("{} {}\n", result, dur);

  for (int i = 0; i < 10'00; ++i)
    result = finalValueAfterOperations2(inp);
  dur = t.timeSinceLastMs();
  fmt::print("{} {}\n", result, dur);

  for (int i = 0; i < 10'00; ++i)
    result = finalValueAfterOperations2b(inp);
  dur = t.timeSinceLastMs();
  fmt::print("{} {}\n", result, dur);
}