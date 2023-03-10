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
  int i = 1;
  while(i <= array.size())
  {
    int ans = INT32_MAX;
    std::vector<int> a;
    if(array[i] >= 10 && array[i] < 100)
    {
      if(array[i -1] >= 10 && array[i - 1] < 100)
      {
        if(array[i] > array[i - 1])
        {
          array.erase(array.begin() + i);
        }
        else
        {
          array.erase(array.begin() + i - 1);
        }
      }
      else
      {
        i++;
      }
    }
    else
    {
      i++; 
    }
  }
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