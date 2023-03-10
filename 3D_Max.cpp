#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <cstdlib>

int processArray(std::vector<int> &array) {
  /* 
   * Do not make any changes outside this function.
   *
   * Modify this function to process `array` as indicated
   * in the question. At the end, return the length of the
   * array.
   *
   * Do not print anything in this function
   * Do not write anything to the standard output
   *
   * Submit this entire program (not just this function)
   * as your answer
   */
  array.push_back(-1);
  int i = 0;
  while(i <= array.size())
  {
    if(array[i] >= 100 && array[i] <= 999 && array[i + 1] >= 100 && array[i + 1] <= 999)
    {
        if(array[i] > array[i + 1])
            array.erase(array.begin() + i + 1);
        else
            array.erase(array.begin() + i);
    }
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