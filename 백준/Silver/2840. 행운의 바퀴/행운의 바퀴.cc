#include <iostream>
#include <deque>
#include <vector>
#include <set>

using namespace std;

int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, K;
	char prnt = '?';
	vector<char> vtr;

	cin >> N >> K;

	deque<char> wheel;
	for (int i = 0; i < N; i++) {
		wheel.push_back('?');
	}

	for (int i = 0; i < K; i++) {
		int change;
		char point;

		cin >> change >> point;

		for (int j = 0; j < change; j++) {
			wheel.push_front(wheel.back());
			wheel.pop_back();
		}

		if (prnt != '!' and wheel[0] == '?' or wheel[0] == point) {
			wheel.pop_front();
			wheel.push_front(point);
		}
		else {
			prnt = '!';

			break;
		}
	}

	for (char w : wheel) {
		if (w != '?') {
			vtr.push_back(w);
		}
	}

	set<char> s(vtr.begin(), vtr.end());

	if (s.size() != vtr.size()) {
		prnt = '!';
	}

	if (prnt == '?') {
		for (int i = 0; i < N; i++) {
			cout << wheel[i];
		}
	}
	else {
		cout << prnt;
	}
}