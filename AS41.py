import random

def generate_random_binary_string(length):
    return ''.join(random.choice('01') for _ in range(length))

def add_parity_bit(binary_string):
    # Calculate the parity bit (even or odd parity)
    parity_bit = '1' if binary_string.count('1') % 2 == 0 else '0'
    return parity_bit + binary_string

def check_parity(binary_string, guess):
    # Calculate the expected parity bit
    expected_parity_bit = '1' if binary_string.count('1') % 2 == 0 else '0'
    
    # Check if the guess matches the expected parity
    return guess == expected_parity_bit

def main():
    num_questions = 5
    
    print("Welcome to the Parity Bit Checker Quiz!")
    print("You will be given binary strings with a parity bit, and you need to guess if the parity is even (E) or odd (O).")
    
    score = 0
    
    for _ in range(num_questions):
        binary_string = generate_random_binary_string(8)  # Generate a random 8-bit binary string
        binary_string_with_parity = add_parity_bit(binary_string)
        
        print("\nBinary String with Parity Bit:", binary_string_with_parity)
        guess = input("Is the parity even (E) or odd (O)? ").strip().upper()
        
        if guess == 'E' or guess == 'O':
            if check_parity(binary_string, guess):
                print("Correct! The parity is", guess)
                score += 1
            else:
                print("Incorrect! The correct answer is", 'E' if binary_string.count('1') % 2 == 0 else 'O')
        else:
            print("Invalid input. Please enter 'E' for even or 'O' for odd parity.")
    
    print("\nQuiz completed! Your score:", score, "out of", num_questions)

if __name__ == "__main__":
    main()
