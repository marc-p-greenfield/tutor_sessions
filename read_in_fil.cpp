#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int Number;
	string Holder;
    vector<char> test_vector;
	ifstream Test ("temp_data.txt");
	if (Test.is_open())
	{
        char c;
        while(Test.get(c)){
            test_vector.push_back(c);
        }
	}

    int size = test_vector.size() - 1;
    cout << size << endl;
    cout << test_vector[3] << endl;
	Test.close();
	return 0;
}
