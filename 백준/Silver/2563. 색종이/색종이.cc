#include <iostream>
using namespace std;
int arr[101][101];

int main() {
	int cnt = 0;
	int n = 0;
	int x, y;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> x >> y;
		for (int i = x; i < x+10; i++) {
			for (int k = y; k < y+10; k++) {
				if (arr[i][k] == NULL)
				{
					arr[i][k] = 1;
					cnt += 1;
				}
			}
		}
	}
	cout << cnt;
	return 0;
}