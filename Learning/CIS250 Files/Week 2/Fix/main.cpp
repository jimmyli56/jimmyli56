#include <iostream>
using namespace std;

int main() {
    // Declare and Initialize Variables
    int height = 0;
    int feet = 0; // Add a missing semicolon here
    int inches = 0;

    // Prompt for height
    cout << "Enter your height in inches: "; // Use << for output
    cin >> height; // Use the correct variable name "height"

    // Calculate Height in feet and inches
    feet = height / 12; // Use = for assignment, not /
    inches = height % 12;

    // Print out height in feet and inches
    cout << "You are " << feet << " feet and " << inches << " inches"; // Use << for output

    cout << "\nJimmy Li - 8/31/23" << endl;

    return 0;
}

