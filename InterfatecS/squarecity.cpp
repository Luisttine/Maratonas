#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, total;
    cin >> n;
    total =0;
    while(n>0){
        int count = ((n+(n-2))*2)-2;
        if(count > 0){
            total += count;
        }
        n-=4;
    }
    cout << total << '\n';
}
