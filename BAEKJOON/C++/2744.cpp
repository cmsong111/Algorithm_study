#include <stdio.h>
#include <string.h>

int main(void) {
  char str[101];
  scanf("%s", str);
  int len = strlen(str);
  for (int i = 0; i < len; i++) {
    if (65 <= str[i] && str[i] <= 90) {
      printf("%c", str[i] + 32);
    } else {
      printf("%c", str[i] - 32);
    }
  }
  return 0;
}