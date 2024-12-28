#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int n, k;
	int arr[1001];
	cin >> n >> k;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	sort(arr, arr + n);
	cout << arr[n - k] << endl;

	return 0;
}