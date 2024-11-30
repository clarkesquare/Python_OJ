#include <iostream>
using namespace std;

int main() {
	int a, i, sum = 0;
	
	for (i = 1; i <= 5; i++)
	{
		cin >> a;
		sum += a;
	}
	cout << sum << endl;
}