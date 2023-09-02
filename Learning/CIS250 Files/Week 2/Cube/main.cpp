#include <iostream> // Include the necessary library for input and output

int main() {
    int N; // Declare a variable to store user input

    // Ask user to enter an integer
    std::cout << "Please enter an integer: ";
    std::cin >> N; // Read the integer from the user

    // Calculate the cube of the number
    int result = N * N * N;

    // Print the result
    std::cout << "The cube of " << N << " is: " << result << std::endl;
    // Print my name and the date the program was written
    std::cout << "\nJimmy Li - 8/31/23" << std:: endl;
    return 0; // Return 0 to indicate the program ran successfully
} // end of program