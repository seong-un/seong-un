#include <string>
#include <vector>
#include <cstdio>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    string apb, bpa;
    apb = to_string(a) + to_string(b);
    bpa = to_string(b) + to_string(a);
    
    if (stoi(apb) < stoi(bpa)) answer = stoi(bpa);
    else answer = stoi(apb);
    
    
    return answer;
}