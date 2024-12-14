#include <iostream>
using namespace std;

int main() {
    int arr[101][101];
    int max = 0;
    int x, y;
    int i = 0, j = 0;

    // arr1에 입력
    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++)
            cin >> arr[i][j];

    for (int i = 0; i < 9; i++)
        for (int j = 0; j < 9; j++)
            if (max <= arr[i][j])
            {
                max = arr[i][j];
                x = i + 1;
                y = j + 1;
            }
    
    cout << max << endl;
    cout << x << " " << y;

    return 0;
}