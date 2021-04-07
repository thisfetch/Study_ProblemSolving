#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };
int main(void) {
	ios::sync_with_stdio(0), cin.tie(0);
	int F;
	cin >> F;
	for (int i = 0; i < F; i++) {
		int board[50][50] = { 0, };
		bool vis[50][50] = { 0, };
		int M, N, K;
		cin >> M >> N >> K;

		for (int i = 0; i < K; i++) {
			int x, y;
			cin >> x >> y;
			board[x][y] = 1;
		}
		int bug = 0;
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (board[i][j] == 0 || vis[i][j]) continue;
				bug++;
				queue<pair<int, int>> q;
				vis[i][j] = 1;
				q.push({ i, j });
				while (!q.empty()) {
					pair<int, int> cur = q.front(); q.pop();
					for (int dir = 0; dir < 4; dir++) {
						int nx = dx[dir] + cur.X;
						int ny = dy[dir] + cur.Y;
						if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
						if (board[nx][ny] != 1 || vis[nx][ny]) continue;
						vis[nx][ny] = 1;
						q.push({ nx, ny });
					}
				}
			}
		}
		cout << bug << '\n';
	}
}