#include <bits/stdc++.h>

using namespace std;

int n, r, s, t, p;

bool dfs(vector<int> comodos, vector<vector<int>> passagem, int atual, vector<bool> &passou){
    passou[atual] = true;
    if(comodos[atual] == 1){
        return false;
    }
    if(atual == s){
        return true;
    }
    for(int x: passagem[atual]){
        if(!passou[x] && dfs(comodos, passagem, x, passou)){
            return true;
        }
    }
    return false;
}

int main(){
    cin >> n >> r >> s >> t;
    vector<int> comodos(n+1);
    vector<bool> passou(n+1, false);
    vector<vector<int>> passagem(n+1);
    for(int i=0;i<t;++i){
        int j;
        cin >> j;
        comodos[j] = 1;
    }
    cin >> p;
    for(int i=0;i<p;++i){
        int a, b;
        cin >> a >> b;
        passagem[a].push_back(b);
    }
    bool is_safe = dfs(comodos, passagem, r, passou);
    if(is_safe){
        cout << "PROSSEGUIR\n";
    }else{
        cout << "ABORTAR\n";
    }
}
