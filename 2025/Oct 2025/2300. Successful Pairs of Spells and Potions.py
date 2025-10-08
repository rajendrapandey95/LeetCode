#include <bits/stdc++.h>
using namespace std;
#define ll long long
int dp[1<<20][2],n,m;
char g[21][21];

int mask0(){
    int r=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if(g[i][j]=='1')r|=1<<(i*m+j);
    return r;
}
bool get(int msk,int i,int j){
    return i>=0&&j>=0&&i<n&&j<m&&!(msk&(1<<(i*m+j)));
}
bool pos(int msk,int i){
    int r=i/m,c=i%m;
    return get(msk,r-1,c)||get(msk,r+1,c)||get(msk,r,c-1)||get(msk,r,c+1);
}
bool possible(int msk){
    for(int i=0;i<n*m;i++)
        if(pos(msk,i))return 1;
    return 0;
}
int go(int msk,int p){
    if(dp[msk][p]!=-1)return dp[msk][p];
    if(!possible(msk))return dp[msk][p]=p;
    int r=p;
    for(int j=0;j<n*m;j++){
        if(msk&(1<<j))continue;
        if(pos(msk,j)){
            int nm=msk|(1<<j);
            r=p?min(r,go(nm,p^1)):max(r,go(nm,p^1));
        }
    }
    return dp[msk][p]=r;
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    memset(dp,-1,sizeof(dp));
    int q;cin>>n>>m>>q;
    while(q--){
        for(int i=0;i<n;i++)cin>>g[i];
        cout<<(1^go(mask0(),0))<<"\n";
    }
}
