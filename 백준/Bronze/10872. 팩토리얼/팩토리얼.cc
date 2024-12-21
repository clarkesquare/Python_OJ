#include <iostream>
using namespace std;

int main() {
	int answer = 1;
	int n;
	int i;

	cin >> n;
	for (i = 1; i <= n; i++)
	{
		answer *= i;
	}

	cout << answer;

	return 0;
}