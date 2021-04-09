#include <bits/stdc++.h>
using namespace std;

int arr[500002];
stack<pair<int, int>> st;

int main(void) {
	ios::sync_with_stdio(0), cin.tie(0);
	int n, height;

	cin >> n;

	cin >> height;
	st.push({ 0, height });

	for (int i = 1; i < n; i++) {
		cin >> height;
		
		if (st.top().second < height) {
			while (!st.empty() && st.top().second < height) st.pop();
			if (st.empty()) {
				arr[i] = 0;
			}
			else {
				arr[i] = st.top().first + 1;
				if (st.top().second == height) st.pop();
			}
		}
		else {
			arr[i] = st.top().first + 1;
		}
		st.push({ i, height });
	}

	for (int i = 0; i < n; i++) {
		cout << arr[i] << ' ';
	}
}