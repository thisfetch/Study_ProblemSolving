#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0), cin.tie(0);
	stack<char>st;
	string pro;
	int stick = 0, count = 0;
	cin >> pro;

	for (auto c : pro) {
		if (c == '(') {
				stick++;
				count++;
				st.push(c);
		}
		else if (c == ')') {
			if (st.top() == '(' && stick == 1) {
				stick--;
				count--;
				st.push(c);
			}
			else if (st.top() == '(' && stick != 1) {
				stick--;
				count--;
				count += stick;
				st.push(c);
			}
			else if (st.top() == ')') {
				stick--;
				st.push(c);
			}
		}
	}
	cout << count;
}