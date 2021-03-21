#include <bits/stdc++.h>
using namespace std;
const int MAX = 10001;

int func(int n) {
	int sum = n;
	while (n != 0) {
		sum += n % 10;
		n = n / 10;
	}

	return sum;
}

int main(void) {
	int arr[MAX] = { 0, };

	for (int i = 1; i <= 10000; i++) {
		int tmp = func(i);
		if (tmp <= 10000) arr[tmp] = 1;
	}

	for (int i = 1; i <= 10000; i++) {
		if (arr[i] != 1) {
			cout << i << '\n';
		}
	}

}