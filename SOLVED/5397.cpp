#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int N;
	cin >> N;
	while (N--) {
		string word;
		cin >> word;
		list<char> L;

		list<char>::iterator itr = L.end();

		for (auto c : word) {
			if (c == '<') {
				if (itr == L.begin()) continue;
				itr--;
			}
			else if (c == '>') {
				if (itr == L.end()) continue;
				itr++;
			}
			else if (c == '-') {
				if (itr == L.begin()) continue;
				itr = L.erase(--itr);
			}
			else {
				L.insert(itr, c);
			}
		}

		for (auto it = L.begin(); it != L.end(); it++)
			cout << *it;
		cout << '\n';
		L.clear();
	}
	return 0;
}