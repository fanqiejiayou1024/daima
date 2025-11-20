//
// Created by fanqi on 24-10-11.
//
#include <bits/stdc++.h>
using namespace std;
int main() {
    char a[14], mod[12] = "0123456789X";
    scanf("%s",a);
    //printf("%c\n",a[1]);
    //printf("%d",);
    int j = 1,ib = 0;
    for (int i = 0;i <= 11;i++) {//0-670-82162  -4    11位
        //printf("%c\n\n",a[i]);
        if (a[i] != '-') {
            ib += int(a[i] - '0') * j;
            j++;
        }
    }
    int acc = ib % 11;
    if (mod[acc] = a[12]) {
        cout << "Right";
    }else {
        a[10] = mod[acc];
        printf("%s",a);
    }
    return 0;
}