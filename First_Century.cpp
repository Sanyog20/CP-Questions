#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <cstdlib>

int processArray(std::vector<int> &array)
{
    array.push_back(-99);
    int s = 0;
    while(s <= array.size())
    {
        if(array[s - 1] >= 100 && s != 0 && array[s] >= 100)
            array.erase(array.begin() + s);
        else
            s++;
    }
    array.pop_back();
    return array.size();
}

int main(void) {
    std::vector<int> array;
    int val;
    while (std::cin >> val)
    {
        if (val < 0) break;
        array.push_back(val);
    }
    int new_len = processArray(array);
    for(std::vector<int>::iterator a = array.begin(); a != array.end(); a++)
    {
        std::cout << *a << std::endl;
    }
    return 0;
}