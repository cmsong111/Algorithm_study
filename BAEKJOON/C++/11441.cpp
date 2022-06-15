#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <stdio.h>

using namespace std;

int main(void) {
	vector<int> arr;

	int count;
	int temp;
	scanf("%d", &count);
	scanf("%d", &temp);
	arr.push_back(temp);
	for (int i = 1; i < count; i++) {
		int temp;
		scanf("%d", &temp);
		arr.push_back(temp+arr[i-1]);
	}

	//출력부
	scanf("%d", &count);
	while(count--){
		int start, end;
		scanf("%d %d", &start, &end);
		if (start == 1) {
			printf("%d\n", arr[end - 1]);
		}
		else {
			printf("%d\n", arr[end - 1] - arr[start - 2]);
		}
	}


	return 0;

}