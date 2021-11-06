#include <bits/stdc++.h>

using namespace std;

int main(){
    vector<int> pixeis;
    int soma = 0;
    int x;
    while(cin >> x){
        pixeis.push_back(x);
        soma+=x;
    }
    cout.precision(3);
    for(int i: pixeis){
        cout << fixed <<  double(i)/double(soma) << endl;
    }
}