#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>

using namespace std;

int main(void) {
	int count, temp;
	vector<char> arr_result;
	vector<int> arr_stack;
	vector<int> arr_first;
	vector<int> arr_target;



	scanf("%d", &count);

	for (int i = count; i > 0; i--) {
		arr_first.push_back(i);
	}

	for (int i = 0; i < count; i++) {
		scanf("%d", &temp);
		arr_target.push_back(temp);
	}


	arr_stack.push_back(arr_first.back());
	arr_first.pop_back();
	arr_result.push_back('+');

	int i = 0;
	int error = 0;
	while (i < count) {
		if (arr_stack.size() == 0) {
			if (arr_first.size() == 0) {
				error++;
				break;
			}
			arr_result.push_back('+');
			arr_stack.push_back(arr_first.back());
			arr_first.pop_back();
		}
		if (arr_target[i] == arr_stack.back()) {
			arr_result.push_back('-');
			arr_stack.pop_back();
			i++;
		}
		else {
			if (arr_first.size() == 0) {
				error++;
				break;
			}
			arr_result.push_back('+');
			arr_stack.push_back(arr_first.back());
			arr_first.pop_back();
		}
	}


	if (error != 0) {
		printf("NO");
	}
	else {
		for (i = 0; i < arr_result.size(); i++) {
			printf("%c\n", arr_result[i]);
		}
	}

	return 0;

}