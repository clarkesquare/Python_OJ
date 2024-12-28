#include <iostream>
using namespace std;

int main() {
	int a, b, c;
	cin >> a >> b >> c;
	int total = a * b * c;
	int num[10] = { 0 };

	while (total > 0)
	{
		num[total % 10]++;
		total /= 10;
	}

	for (int i = 0; i < 10; i++) {
		cout << num[i] << endl;
	}

	return 0;
}