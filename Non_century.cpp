# include <iostream>
# include <bits/stdc++.h>
# define int               long long
using namespace std;
 
signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<int> a;
    int ans = 0;
    while(1)
    {
        int x;
        cin >> x;
        if(x < 0)
        {
            break;
        }
        else
        {
            a.push_back(x);
            if(x < 100)
            {
                if(x > ans)
                {
                    ans = x;
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}