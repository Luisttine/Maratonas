#include <bits/stdc++.h>
using namespace std;

int c, n;
int main(){
  cin >> c;
  for(int caso=1;caso<=c;++caso){
    cin >> n;
    vector<int> arr;
    for(int i=0;i<n;++i){
      int j;
      cin >> j;
      arr.push_back(j);
    }
    int l=0, h=0;
    for(int i=1;i<n;++i){
      if(arr[i-1] < arr[i]){
        h++;
      } else if(arr[i-1] > arr[i]){
        l++;
      }
    }
    printf("Case %i: %i %i\n",caso,h,l);
  }
}
