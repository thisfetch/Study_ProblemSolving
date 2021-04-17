#include <bits/stdc++.h>
using namespace std;
#define MAX 68

string screen[MAX];
string ans;

bool check(int row, int col, int num) {
	bool isSame = true;
	char start = screen[row][col];
	for (int i = row; i < row + num; i++) {
		for (int j = col; j < col + num; j++) if (screen[i][j] != start) return false;
	}
	if (isSame) ans += start;
	return true;
}

void div(int row, int col, int num) {
	if (num == 0) return;
	bool isSame = check(row, col, num);
	if(!isSame)
	{
		num /= 2;
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 2; j++){
				if (i == 0 && j == 0) ans += "("; 
				div(row + (num * i), col + (num * j), num);
				if (i == 1 && j == 1) ans += ")";
			}
		}
	}
}

int main(void) {
	ios::sync_with_stdio(0), cin.tie(0);
	int N;
	cin >> N;

	for (int i = 0; i < N; i++) cin >> screen[i];

	div(0, 0, N);
	cout << ans;
}
