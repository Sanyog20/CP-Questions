#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <cstdlib>

int processArray(std::vector<int> &array) {
  int i = 0;
  array.push_back(100);
  while(i <= array.size())
  {
    if(array[i] < 10 && array[i + 1] < 10 && array[i + 1] > 0)
      array.erase(array.begin() + i);
    else
        i++;
  }
  array.pop_back();
  return array.size();
}

int main(void) {
  std::vector<int> array;
  int val;
  while (std::cin >> val) {
    if (val < 0) break;
    array.push_back(val);
  }
  int new_len = processArray(array);
  for(std::vector<int>::iterator a = array.begin(); a != array.end(); a++) {
    std::cout << *a << std::endl;
  }
  return 0;
}
