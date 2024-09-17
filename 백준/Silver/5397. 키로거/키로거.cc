#include <iostream>
#include <sstream>
#include <deque>
#include <vector>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int T = 0;
	cin >> T;

	for (int t = 0; t < T; t++) {
		string L;
		cin >> L;
		vector<char> left;
		deque<char> right;

		for (char l : L) {
			if (l == '<') {
				if (!left.empty()) {
					right.push_front(left.back());
					left.pop_back();
				}
			}
			else if (l == '>') {
				if (!right.empty()) {
					left.push_back(right.front());
					right.pop_front();
				}
			}
			else if (l == '-') {
				if (!left.empty()) {
					left.pop_back();
				}
			}
			else {
				left.push_back(l);
			}
		}

		for (char i : left) {
			cout << i;
		}

		for (char i : right) {
			cout << i;
		}

		cout << endl;
	}

	return 0;
}