#include <iostream>
#include <string>

using namespace std;

int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int i = 0;
	string str;
	while (i < 100)
	{
		getline(cin, str);
		cout << str + '\n';
		i++;
	}
}