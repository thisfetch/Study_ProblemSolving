#include <bits/stdc++.h>

using namespace std;


int main(void) {
	ios::sync_with_stdio(0), cin.tie(0);
	int N, M;
	map<int, string> col;
	map<string, int> col2;

	string pokemon, ans;
	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		cin >> pokemon;
		col.insert(make_pair(i, pokemon));
		col2.insert(make_pair(pokemon, i));
	}
	for (int i = 1; i <= M; i++) {
		cin >> pokemon;
		if (atoi(pokemon.c_str()) == 0) {
			cout << col2[pokemon] << "\n";
		}
		else {
			cout << col[atoi(pokemon.c_str())] << "\n";
		}
	}
}