#include <stdio.h>

#define PI 3.141592

int main(void){
    double a1;
    double a2;
    scanf("%lf",&a1);
    scanf("%lf",&a2);
    printf("%.6lf",a1*2 + a2*2*PI);
    return 0;
}