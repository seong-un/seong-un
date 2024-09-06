#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	 ios::sync_with_stdio(false);
	 cin.tie(NULL);

	int N, xi, yi;

	cin >> N;

	vector<vector<int>> xyi(N);
	for (int i = 0; i < N; i++) {
		cin >> xi >> yi;
		xyi[i].push_back(xi);
		xyi[i].push_back(yi);
	}

	sort(xyi.begin(), xyi.end());

	for (int i = 0; i < N; i++) {
		cout << xyi[i][0] << " " << xyi[i][1] << '\n';
	}

	return 0;
}