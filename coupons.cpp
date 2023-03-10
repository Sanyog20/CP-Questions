#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s = "dccccd";
    int k = 3;
    long long int max_cost = 0;
    for(int i = 0; i < s.length() - k; i++)
    {
        int cost[26] = {0};
        for(int j = 0; j < k; j++)
        {
            int t = int(s[i + j]) - 97;
            cost[t]++;
        }
        long long int c = 0;
        for(int j = 0; j < 26; j++)
        {
            if(cost[j] != 0)
                c = c + (int(pow(j + 1, cost[j])) % 1000000007) % 1000000007;
        }
        if(c > max_cost)
        {
            max_cost = c;
        }
    }
    cout << max_cost;
    return 0;
}