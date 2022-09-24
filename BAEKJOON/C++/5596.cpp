#include <stdio.h>

int main(void) {
    int S = 0;
    int T = 0;
    int temp;
    for (int i = 0; i < 4; i++) {
        scanf("%d", &temp);
        S = S + temp;
    }
    for (int i = 0; i < 4; i++) {
        scanf("%d", &temp);
        T = T + temp;
    }

    S > T ? printf("%d", S) : printf("%d", T);

    return 0;
}