// https://www.hackerrank.com/challenges/maximum-draws/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    for(int i = 0;i != n; ++i) {
        int socks_N;
        cin >> socks_N;
        cout << (socks_N + 1) << endl;
    }
    return 0;
}
