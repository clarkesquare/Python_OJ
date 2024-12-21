#include <iostream>
using namespace std;

int main(void)
{
	int n, answer = 0, tmp, bonus = 0;
	cin >> n;

	for (int i = 1; i < n + 1; i++)
	{
		cin >> tmp;
		if (tmp == 1)
		{
			bonus++;
			answer += bonus;
		}
		else
		{
			bonus = 0;
		}
	}
	cout << answer;

	return 0;
}