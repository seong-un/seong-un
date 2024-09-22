#include <iostream>
#include <unordered_map>
#include <set>

using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N;
	cin >> N;

	unordered_map<int, int> map_problem;
	set<pair<int, int>> set_problem;

	for (int n = 0; n < N; n++) {
		int P, L;

		cin >> P >> L;

		map_problem[P] = L;
		set_problem.insert({ L, P });
	}

	int M;
	cin >> M;

	for (int m = 0; m < M; m++) {
		string command;
		int P, L;
		int x;

		cin >> command;
		
		if (command == "add") {
			cin >> P >> L;
			set_problem.insert({ L, P });
			map_problem[P] = L;
		}
		else if (command == "recommend") {
			cin >> x;
			if (x == -1) {
				cout << (*set_problem.begin()).second << endl;
			}
			else if (x == 1) {
				cout << (*prev(set_problem.end())).second << endl;
			}
		}
		else if (command == "solved") {
			cin >> P;
			set_problem.erase({ map_problem[P], P });
			map_problem.erase(P);
		}
	}

	return 0;
}