#include <iostream>
using namespace std;

int main(void)
{
	int i = 0;
	int n = 0;
	int answer = 0;
	int minimum = 100;

	for (i = 0; i < 7; i++)
	{
		cin >> n;
		if (n % 2 == 1)
		{
			answer += n;
			if (minimum > n)
			{
				minimum = n;
			}
		}
	}

	if (answer != 0)
	{
		cout << answer << endl << minimum;
	}
	else
	{
		cout << -1;
	}

	return 0;
}