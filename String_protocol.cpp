# include <iostream>
# include <bits/stdc++.h>
using namespace std;
 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        int time = 0;
        for(int i = 0; i < n; i++)
        {
            if(s[i] == s[i + 1])
            {
                time = time + 1;
                i++;
            }
            else
            {
                time = time + 1;
            }
        }
        cout << time << endl;
    }
    return 0;
}