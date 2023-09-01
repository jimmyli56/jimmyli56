#include <iostream> // Include the necessary library for input and output

int main() {
    int N; // Declare a variable to store the user's input

    // Prompt the user to enter an integer
    std::cout << "Please enter an integer: ";
    std::cin >> N; // Read the integer from the user

    // Calculate the cube of the number
    int result = N * N * N;

    // Print the result
    std::cout << "The cube of " << N << " is: " << result << std::endl;

    return 0; // Return 0 to indicate successful program execution
}

