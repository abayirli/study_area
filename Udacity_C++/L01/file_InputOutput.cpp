#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){


	string line;

	ofstream myfileI("input.txt", ios::app);

	if(myfileI.is_open()){

		myfileI << "\nAdding a new line \n";
		myfileI << "Adding another new line\n";

		myfileI.close();
	}

	else{
		cout << "File cannot be opened for write..." << endl;
	}

	ifstream myfileO("input.txt", ios::app);
	if(myfileO.is_open()){

		while(getline(myfileO, line)){
			cout << line << endl;
		}
		myfileO.close();
	}
	else{
		cout << "File cannot be opened for read..." << endl;
	}

	return 0;
}
