#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
int main(void)
{
    std::string s1, s2, s3;
    std::string ans = "NO";

    cin >> s1 >> s2 >> s3;

    std::string str;
    str = s1[0] + s2[0] + s3[0];

    //transform(str.begin(), str.end(), str.begin(), toupper);

    cout << str << endl;
}
