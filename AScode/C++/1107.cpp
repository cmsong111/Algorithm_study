#include <stdio.h>

int main(void) {
    int testcase, sizeX, sizeY;

    scanf("%d", &testcase);
    while (testcase--) {
        scanf("%d %d", &sizeX, &sizeY);
        for (int i = 0; i < sizeX; i++) {
            for (int ii = 0; ii < sizeY; ii++) {
                printf("%d ", i + ii);
            }
            printf("\n");
        }
        printf("\n");
    }

    return 0;
}