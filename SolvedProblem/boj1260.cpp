#include <bits/stdc++.h>
using namespace std;
#define MAX 27
#define X first
#define Y second
int board[MAX][MAX];
bool vis[MAX][MAX] = { false, };
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int main(void) {
	int n;
	vector<int> v;
	int num = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			scanf("%1d", &board[i][j]);
	
	for (int i = 0; i < n; i++) 
		for (int j = 0; j < n; j++) {
			if (board[i][j] == 0 || vis[i][j] == true) continue;
			num++;
			queue<pair<int, int>> q;
			vis[i][j] = true;
			q.push({ i, j });
			int home = 0;
			while (!q.empty()) {
				auto cur = q.front(); q.pop();
				home++;
				for (int dir = 0; dir < 4; dir++) {
					int nx = cur.X + dx[dir];
					int ny = cur.Y + dy[dir];
					if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
					if (vis[nx][ny] == true || board[nx][ny] != 1) continue;
					vis[nx][ny] = 1;
					q.push({ nx, ny });
				}
			}
			v.push_back(home);
		}
	sort(v.begin(), v.end());
	cout << num << '\n';
	for (auto c : v) {
		cout << c << '\n';
	}
	return 0;
}