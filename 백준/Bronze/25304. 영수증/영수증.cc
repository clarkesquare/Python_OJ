#include <iostream>
using namespace std;

int main() {
	int total, i, n, a, b, tmp = 0;
	
	cin >> total;
	cin >> n;
	for (i = 1; i <= n; i++)
	{
		cin >> a >> b;
		tmp += a * b;

	}
	if (total == tmp)
	{
		cout << "Yes" << endl;
	}
	else
	{
		cout << "No" << endl;
	}
}