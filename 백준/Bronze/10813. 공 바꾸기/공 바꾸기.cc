#include <iostream>
using namespace std;
int main()
{
	int n, m;
	int basket[100];
	int tmp = 0;
	cin >> n >> m;

	for (int a = 0; a <= n; a++)
	{
		basket[a] = a + 1;
	}

	for (int a = 0; a < m; a++)
	{
		int i, j;
		cin >> i >> j;
		tmp = basket[i - 1];
		basket[i - 1] = basket[j - 1];
		basket[j - 1] = tmp;
	}

	for (int a = 0; a < n; a++)
	{
		cout << basket[a] << " ";
	}
}