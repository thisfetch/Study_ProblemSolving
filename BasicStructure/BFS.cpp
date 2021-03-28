#include<iostream>
#include<utility>
#include<string>
using namespace std;

void same(pair<int, string> a, pair<int, string> b) {
	if (a == b)
		cout << "true" << endl;
	else
		cout << "false" << endl;
}
void comp(pair<int, string>a, pair<int, string> b) {
	if (a < b)
		cout << "true" << endl;
	else
		cout << "false" << endl;
}

int main(void) {
	pair<int, string> p1 = make_pair(1, "BlockDMask");
}