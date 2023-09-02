#include <iostream>
using namespace std;

int main() { // Corrected int
    int height = 0; // Corrected variable name from inT to int
    int feet = 0; // Corrected int
    int inches = 0;
    // Prompt for height
    cout << "Enter your height in inches: "; // Changed '>>' to '<<' for cout
    cin >> height; // Corrected variable name "Height" to "height"
    // Calculate Height in feet and inches
    feet = height / 12; // Corrected the assignment operator '/' to '='
    inches = height % 12;
    // Print out height in feet and inches
    cout << "You are " << feet << " feet and " << inches << " inches"; // Corrected the '<<' operator for cout
    // system("pause"); //Unused since I am using a Mac
    cout << "\nJimmy Li - 8/31/23" << endl;
    return 0;
} // end of program

