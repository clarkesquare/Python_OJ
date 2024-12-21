#include <iostream>
using namespace std;

int main(void)
{
	int n, maximum = 0;
	int x, y;

	for (int i = 1; i <= 9; i++)
	{
		for (int j = 1; j <= 9; j++)
		{
			cin >> n;
			if (maximum <= n)
			{
				maximum = n;
				x = i;
				y = j;
			}

		}
		cout << endl;

	}
	cout << maximum << endl << x << " " << y;

	return 0;
}