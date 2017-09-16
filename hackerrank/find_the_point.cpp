//https://www.hackerrank.com/challenges/find-point/problem

#include <iostream>

using namespace std;

int main()
{
  int n;
  cin >> n;
  for(int i = 0; i != n; ++i) {
    int x1,y1,x2,y2;
    cin >> x1 >> y1 >> x2 >> y2;
    cout << (2 * x2) - x1 << " " << (2 * y2) - y1 << endl; 
  }
}
