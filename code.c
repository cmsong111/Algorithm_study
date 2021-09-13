#include<stdio.h>

int main(void)
{
	int x, y, z;
	
	printf("삼각형의 세변을 입력하시오\n");
	scanf("%d%d%d", &x, &y, &z);

	if (z < x + y && x < z + y && y < x + z) // 삼각형의 성립조건
		;
	else
	{
		printf("삼각형이 아닙니다");
		return 0;
	}

	
	if (x == y) // x = y으로 시작
	{
		if (y == z) // 정삼각형 조건
			printf( "정삼각형");
		else //이등변 삼각형 조건 1
			printf("이등변 삼각형");
	}
	else //x,y이외의 다른변이 같을 때
	{
		if (x == z && z != y) //이등변 삼각형 조건 2
			printf("이등변 삼각형");
		else if (y == z && x != z) //이등변 삼각형 조건 3
			printf("이등변 삼각형");
		else //일반 삼각형일 떄
			printf("일반 삼각형");

	}
	return 0;
}
