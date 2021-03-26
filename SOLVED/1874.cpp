#include<bits/stdc++.h>
using namespace std;

int main() {
    char printer[200000];
    int n, el, max(0), ptr(0);
    
    cin >> n;

    stack<int> s;
    while (n--) {
        std::cin >> el;
        if (el > max) {
            for (int i = max + 1; i <= el; i++) {
                s.push(i);
                printer[ptr++] = '+';
            }
        }
        else
            if (s.top() != el) {
                cout << "NO";
                return 0;
            }
        s.pop();
        printer[ptr++] = '-';
       if (max < el) max = el;
    }
    for (int i = 0; i < ptr; i++) std::cout << printer[i] << "\n";

    return 0;
}
