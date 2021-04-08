#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
string board[100];
bool vis[100][100];
bool visx[100][100];
int n;
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

int main(void) {
	ios::sync_with_stdio(0), cin.tie(0);
	int color = 0, colorx = 0;
	cin >> n;
	for (int i = 0; i < n; i++) cin >> board[i];
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (vis[i][j]) continue;
			color++;
			queue<pair<int, int>> q;
			vis[i][j] = true;
			q.push({ i, j });
			while (!q.empty()) {
				auto cur = q.front(); q.pop();
				for (int dir = 0; dir < 4; dir++) {
					int nx = cur.X + dx[dir];
					int ny = cur.Y + dy[dir];
					if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
					if (vis[nx][ny] == true || board[nx][ny] != board[cur.X][cur.Y]) continue;
					vis[nx][ny] = true;
					q.push({ nx, ny });
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (board[i][j] == 'G') {
				board[i][j] = 'R';
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (visx[i][j]) continue;
			colorx++;
			queue<pair<int, int>> q;
			visx[i][j] = true;
			q.push({ i, j });
			while (!q.empty()) {
				auto cur = q.front(); q.pop();
				for (int dir = 0; dir < 4; dir++) {
					int nx = cur.X + dx[dir];
					int ny = cur.Y + dy[dir];
					if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
					if (visx[nx][ny] == true || board[nx][ny] != board[cur.X][cur.Y]) continue;
					visx[nx][ny] = true;
					q.push({ nx, ny });
				}
			}
		}
	}
	cout << color << ' ' << colorx;
}