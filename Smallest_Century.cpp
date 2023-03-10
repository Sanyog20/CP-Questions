# include <iostream>
# include <bits/stdc++.h>
# define int long long
using namespace std;
 
signed main()
{
    int answer = INT16_MAX;
    int element;
    while(1)
    {
        cin >> element;
        if(element < 0)
        {
            break;
        }
        else
        {
            if(element > 100)
            {
                if(element < answer)
                {
                    answer = element;
                }
            }
        }
    }
    if(answer == INT16_MAX)
        cout << 0 << endl;
    else
        cout << answer << endl;
    return 0;
}