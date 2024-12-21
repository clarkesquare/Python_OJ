#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	vector<int> v(3);
	cin >> v[0] >> v[1] >> v[2];

	sort(v.begin(), v.end());
	cout << v[0] << ' ' << v[1] << ' ' << v[2];

	return 0;
}