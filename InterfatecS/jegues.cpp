#include <bits/stdc++.h>

using namespace std;

map<int, string> t1;
map<int, string> t2;
map<int, string> t3;


int main(){
    string s;
    int a,b,c;
    while(cin >> s >> a >> b >> c){
        t1[a] = s;
        t2[b] = s;
        t3[c] = s;
    }
    auto t11 = next(t1.begin(),0);
    auto t12 = next(t1.begin(),1);
    auto t13 = next(t1.begin(),2);
    cout << "T1 " << t11->second <<  " " << t12->second << " " << t13->second << '\n';

    auto t21 = next(t2.begin(),0);
    auto t22 = next(t2.begin(),1);
    auto t23 = next(t2.begin(),2);
    cout << "T2 " << t21->second <<  " " << t22->second << " " << t23->second << '\n';

    auto t31 = next(t3.begin(),0);
    auto t32 = next(t3.begin(),1);
    auto t33 = next(t3.begin(),2);
    cout << "CHEGADA " << t31->second <<  " " << t32->second << " " << t33->second << '\n';
    
}
