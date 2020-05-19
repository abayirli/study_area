/*Write a program that asks a user for five numbers.
**Print out the sum and average of the five numbers.
*/

#include <iostream>
using namespace std;

int main(){
     cout << "Gimme five numbers:" << endl;
     
     int numbers[5];
     for (int i = 0; i < 5; i++){
         cout << "Number "<< i+1 << ": "; cin >> numbers[i];
     }
     
     int sum = 0;
     for(int j=0; j < 5; j++){
         sum += numbers[j];
     }
     cout << "Sum of numbers: " << sum << endl;
     cout << "Average of numbers: " << sum/5.0 << endl; 

     return 0;
}
