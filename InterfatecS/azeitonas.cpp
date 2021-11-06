#include <bits/stdc++.h>

using namespace std;

int x, y;
vector<pair<int, int>> coords;
int main(){
    cin >> x >> y;
    coords.push_back({x,y});
    coords.push_back({y,x});
    coords.push_back({y,-x});
    coords.push_back({x,-y});
    coords.push_back({-x,-y});
    coords.push_back({-y,-x});
    coords.push_back({-y,x});
    coords.push_back({-x,y});


    for(int i=0; i<coords.size(); ++i){
        for(int j=0; j<coords.size(); ++j){
            if(abs(abs(coords[i].first) - abs(coords[i].second)) <= 1 || i!=j && coords[i].first == coords[j].first && coords[i].second == coords[j].second){
                cout << "ERRO\n";
                return 0;
            }
        }
    }

    for(auto c: coords){
        cout << c.first << " " << c.second << '\n';
    }
}
