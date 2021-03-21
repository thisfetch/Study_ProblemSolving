#include <list>
#include <iostream>
using namespace std;

int main(void) {
	list<int> L = { 1,2 }; // 1 2
	auto t = L.begin(); // t�� 1�� ����Ű�� ��
	L.push_front(10); // 10 1 2
	cout << *t << '\n'; // t�� ����Ű�� �� = 1�� ���
	L.push_back(5); // 10 1 2 5
	L.insert(t, 6); // t�� ����Ű�� �� �տ� 6�� ����, 10 6 1 2 5
	t++; // t�� 1ĭ ������ ����, ���� t�� ����Ű�� ���� 2
	t = L.erase(t); // t�� ����Ű�� ���� ����, �� ���� ������ 5�� ��ġ�� ��ȯ
					// 10 6 1 2 5, t�� ����Ű�� ���� 5
	cout << *t << '\n'; // 5
	for(auto i : L) cout << i << ' ';
	cout << '\n';
	for (auto it = L.begin(); it != L.end(); it++)
		cout << *it << ' ';
}