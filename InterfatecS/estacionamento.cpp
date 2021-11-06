#include <bits/stdc++.h>

using namespace std;

const int T = 15; 
map<int, string> vagas;

int get_placa(string s){
    int total = 0;
    for(char c: s){
        total += (int)c;
    }
    return total;
}

int main(){
    string s;
    while(cin >> s){
        int vaga = (get_placa(s)%T)+1;
        if(vagas.find(vaga) == vagas.end()){
            vagas[vaga] = s;
        }
        
    }
    for(auto v: vagas){
        cout << v.first << " " << v.second << "\n";
    }
}
