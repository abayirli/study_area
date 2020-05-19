#include <iostream>

using namespace std;

int main(){
	int TARGET = 33;
	int guess;
	cout << "Gimme some number: " ;
	cin >> guess;

	if(guess == TARGET){
		cout << "You guessed it right!" << endl;
	}
	else if( guess < TARGET){
		cout << "Go up!" << endl;
	}

	else if(guess > TARGET){
		cout << "Go down!" << endl;
	}

	else{
		cout << "There is something wrong!" << endl;
	}

	for(int i=0; i < 5; i++){
		cout << "Hello world" << "\t" << i << endl;
	}

	return 0;
}