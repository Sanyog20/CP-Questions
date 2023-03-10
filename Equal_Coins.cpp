# include <iostream>
using namespace std;

int main()
{
    int t, x, y;
    cin >> t;
    while(t--)
    {
        cin >> x >> y;
        int total = x + (y * 2);
        if(total % 2 == 0)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}