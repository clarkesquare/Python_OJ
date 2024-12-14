#include <iostream>
using namespace std;

int main() {
    int arr1[101][101], arr2[101][101];
    int n, m;
    cin >> n >> m;

    // arr1에 입력
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> arr1[i][j];

    // arr2에 입력
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> arr2[i][j];

    // arr1[i][j], arr2[i][j]를 합한 결과를 줄마다 출력
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cout << arr1[i][j] + arr2[i][j] << " ";

        cout << "\n";
        }
    return 0;
}