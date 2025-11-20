#include <stdio.h>
int main(){
    //输入
    int n;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    //计算
    int max=0;
    for(int i=0;i<n;i++){
        int count=0;
        for(int j=0;j<n;j++){
            if(a[i]==a[j]){
                count++;
            }
        }
        if(count>max){
            max=count;
            a[n]=a[i];
            n++;
        }
    }
    //输出
    printf("%d\n",max);
    for(int i=0;i<n;i++){
        printf("%d ",a[i]);
        if(i==n-1){
            printf("\n");
            break;
        }
    }
    return 0;
}