#include <stdio.h>

void changeBall(int *basket, int n, int m);

int main() {
  int n, m;
  int *basket;
  scanf("%d %d", &n, &m);

  basket = new int[n + 1];

  for (int i = 1; i <= n; i++) {
    basket[i] = i;
  }

  for (int i = 0; i < m; i++) {
    int x, y;
    scanf("%d %d", &x, &y);
    changeBall(basket, x, y);
  }

  for (int i = 1; i <= n; i++) {
    printf("%d ", basket[i]);
  }

  return 0;
}

void changeBall(int *basket, int n, int m) {
  int temp = basket[n];
  basket[n] = basket[m];
  basket[m] = temp;
}