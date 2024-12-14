#include <iostream>
using namespace std;

int main() {
	int n;
	int a;
	int i;
	int j;
	string b;

	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> a >> b;
		for (int j = 0; j < b.length(); j++)
		{
			for (int k = 0; k < a;k++)
				cout << b[j];
		}
		cout << "\n";
	}

	return 0;
}