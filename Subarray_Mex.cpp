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
        int n, k, x;
        cin >> n >> k >> x;
        if(x > k)
        {
            cout << "-1" << endl;
        }
        else if(x == k)
        {
            int t[x];
            for(int i = 0; i < x; i++)
            {
                t[i] = i;
            }
            int count = 0;
            while(count != n)
            {
                cout << t[count % k] << " ";
                count++;
            }
            cout << endl;
        }
        else
        {
            int t[x];
            for(int i = 0; i < x; i++)
            {
                t[i] = i;
            }
            t[x] = x + 1;
            int count = 0;
            while(count != n)
            {
                cout << t[count % (x + 1)] << " ";
                count++;
            }
            cout << endl;
        }
    }
    return 0;
}