#include <bits/stdc++.h>
#define eps 0.000001;
using namespace std;

type struct point {
  double r,x,y;
};
vector<point> points;
double r, d;
int n;
bool inside_pizza(point){
  double dist = sqrt(pow(point.x - 0,2) + pow(point.y - 0,2));
  return (dist+point.r) - r <= eps;
}

int main(){
  cin >> r >> d;
  cin >> n;
  points.clear();
  points.resize(n);
  for(int i=0;i<n;++i){
    cin >> points[i].x >> points[i].y >> points[i].r;
  }
  for(int i=0;i<n;++i){
    if(inside_pizza(points[i])){
      cout << i << endl;
    }
  }
}
