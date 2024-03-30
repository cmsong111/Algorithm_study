#include <stdio.h>

int main() {
  int matrix[5][15] = {
      0,
  };

  for (int i = 0; i < 5; i++) {
    char str[16];
    scanf("%s", str);
    for (int j = 0; str[j] != '\0'; j++) {
      matrix[i][j] = str[j];
    }
  }

  for (int i = 0; i < 15; i++) {
    for (int j = 0; j < 5; j++) {
      if (matrix[j][i] != 0) {
        printf("%c", matrix[j][i]);
      }
    }
  }

  return 0;
}