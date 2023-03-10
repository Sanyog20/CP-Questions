# include <iostream>
# include <bits/stdc++.h>
# define int               long long
using namespace std;
 
signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,x,y;
    cin>>n>>x>>y;
    int len=n;
    vector<int> v;
    int c=abs(x-y);
    if(c==1){
        while(n>0){
            // cout<<n-1<<" ";
            v.push_back(n-1);
            n--;
        }
    }
    else{
        int k=0;
        while(k!=c){
            // cout<<n<<" ";
            v.push_back(n);
            k++;
            n--;
        }
        // cout<<n-2<<" ";
        while(k!=max(x,y)){
            v.push_back(n-2);
            n--;
            k++;
        }
        while(k!=len){
            v.push_back(0);
            k++;
        }
    }
    for(auto i: v){
        cout<<i<<" ";
    }
    return 0;
}