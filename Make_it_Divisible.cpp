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
        int a[n];
        int one = 0, zero = 0, two = 0;
        for(int i = 0; i < n; i++)
        {
            cin >> a[i];
            if(a[i] % 3 == 0)
            {
                zero += 1;
            }
            else if(a[i] % 3 == 1)
            {
                one += 1;
            }
            else
            {
                two += 1;
            }
        }
        int moves = 0;
        moves = moves + min(one, two);
        one = one - moves;
        two = two - moves;
        if(one == 0)
        {
            int t = two % 3;
            if(t == 0)
            {
                moves = moves + two;
            }
            else
            {
                moves = -1;
            }
        }
        else if(two == 0)
        {
            int t = one % 3;
            if(t == 0)
            {
                moves = moves + one;
            }
            else
            {
                moves = -1;
            }
        }
        cout << moves << endl;
    }
    return 0;
}
