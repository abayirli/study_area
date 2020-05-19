#include <iostream>
#include <sstream>
#include <time.h>
#include <cstdlib>

using namespace std;

int main(){
	int target;

	string userString;
	int guess = -1;

	srand(time(NULL)); // set the seed
	target = rand() % 100 + 1; // generate random number

	while(guess != target){
		cout << "Guess a number betweek 0 and 100" << endl;
		getline(cin, userString);

		//convert to int
		stringstream(userString) >> guess;
		cout << userString << endl;

		if(guess > target)
			cout << "Too high!" << endl;
		else if(guess < target)
			cout << "Too low!" << endl;
		else
			cout << "You guessed it right!" << endl;

		if(userString == "q"){
			cout << "goodbye!" << endl;
			cout << "The number was "<< target << endl;
		}
	}

	return 0;
}