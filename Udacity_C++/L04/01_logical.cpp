/*Goal: learn if-else statements in C++*/

#include<iostream>
#include<string>

using namespace std;

int main()
{
    //instead of printing 0 and 1, create an array where 
    //0 = False, 1 = True
    std::string TorF[] = {"False", "True"};
    
    int a = 100;
    int b = 33;
    int c = 33;
    
    //Print out the string values of each relational operation
    std::cout<<"a < b is "<<TorF[a<b];
    std::cout<<"\na > b is "<<TorF[a>b];
    std::cout<<"\na != b is "<<TorF[a!=b];
    std::cout<<"\nc >= b is "<<TorF[c>=b];
    std::cout<<"\nc <= b is "<<TorF[c<=b] << endl;    

    if(a == b){
    	cout << "a is equal to b!" << endl;
    }
    else{
    	cout << "a is not equal to b!" << endl;
    }
    return 0;
}