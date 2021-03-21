#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0), cin.tie(0);
	int m;
	string word;
	cin >> word;
	list<char> L;

	for (auto ch : word) L.push_back(ch);
	
	auto cur = L.end();
	cin >> m;
	while (m--) {
		char cmd;
		cin >> cmd;

		if (cmd == 'P') {
			char var;
			cin >> var;
			L.insert(cur, var);
		}
		else if (cmd == 'L') {
			if (cur != L.begin()) cur--;
		}
		else if (cmd == 'D') {
			if (cur != L.end()) cur++;
		}
		else {
			if (cur != L.begin()) {
				cur--;
				cur = L.erase(cur);
			}
		}
	}
	for (auto ch : L) cout << ch;
}
