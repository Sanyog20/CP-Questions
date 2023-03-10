# include <iostream>
# include <bits/stdc++.h>
# define int               long long
# define endl               '\n'
using namespace std;
 
signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    {
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;
        for(int i = 0; i < n - k + 1; i++)
        {
            if(s[i] == '1')
            {
                for(int j = i; j < i + k; j++)
                {
                    if(s[j] == '0')
                    {
                        s[j] = '1';
                    }
                    else
                    {
                        s[j] = '0';
                    }
                }
            }
        }
        cout << s << endl;
    }
    return 0;
}