#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0), cin.tie(0);
	int tmp(1), ans(0);
	bool x = false;
	string str;
	stack <char> st;

	cin >> str;
	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '(') {
			st.push('(');
			tmp *= 2;
		}
		else if (str[i] == '[') {
			st.push('[');
			tmp *= 3;
		}
		else if (str[i] == ')') {
			if (st.empty()) {
				x = true;
				break;
			}
			if (st.top() == '(') {
				if (str[i - 1] == '(') ans += tmp;
				st.pop();
				tmp /= 2;
			}
			else {
				x = true;
				break;
			}
		}
		else if (str[i] == ']') {
			if (st.empty()) {
				x = true;
				break;
			}
			if (st.top() == '[') {
				if (str[i - 1] == '[') ans += tmp;
				st.pop();
				tmp /= 3;
			}
			else {
				x = true;
				break;
			}
		}
	}

	if (x || !st.empty()) {
		cout << 0 << endl;
	}
	else {
		cout << ans << endl;
	}
}