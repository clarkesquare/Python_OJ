#include <iostream>
using namespace std;

int main(void)
{
	int n;
	int sum = 0;
	int cnt = 0;
	string s;

	cin >> n;	
	for (int j = 0; j < n; j++)
	{
		cin >> s;
		cnt = 0;
		sum = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == 'O')
				cnt++;
			else
				cnt = 0;

			sum += cnt;
		}
		cout << sum << endl;
	}
	return 0;
}