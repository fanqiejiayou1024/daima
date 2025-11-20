//
// Created by fanqi on 24-10-10.
//
#include <iostream>
using namespace std;
int main() {
    short m,t,s;
    cin >> m >> t >> s;
    if(t==0){
        cout << 0 << endl;
    }else if (s % t == 0){
        cout << max(m - s / t,0);
    }else {
        cout << max(m - s / t - 1,0);
    }
    return 0;
}

